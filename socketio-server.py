import eventlet
import socketio
from config import config
from playback import Track
from ytdl import download_track
# from flask import Flask

# app = Flask(__name__)

sio = socketio.Server(cors_allowed_origins="*", logger=True, engineio_logger=True)
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)
    sio.emit('teste', { 'foo': 'bar' })

@sio.event
def play_track(sid, data):
    print('message ', data)
    try:
        url = data.get('url')
        out_file = config.OUT_TMP
        track_info = download_track(url, out_file=out_file, codec=config.CODEC)
        file_path = config.OUT_TMP % dict(id=track_info.get('id'), ext=config.CODEC)
        t = Track(file_path=file_path, codec=config.CODEC, info=track_info)
        print('emiting playing_now')
        sio.emit('playing_now', { 'track': track_info['title'] }, callback=lambda x: print(x))
        t.play()
    except Exception as e:
        print(e)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)