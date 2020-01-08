from playback import Track
from ytdl import download_track
from config import config
from time import time
from utils import clear_dir
from server import app
import os
import eventlet

url = 'https://www.youtube.com/watch?v=BME88lS6aVY'


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
    clear_dir(dir_path=config.TMP_DIR)
    try:
        out_file = config.OUT_TMP
        track_info = download_track(url, out_file=out_file, codec=config.CODEC)
        file_path = config.OUT_TMP % dict(id=track_info.get('id'), ext=config.CODEC)
        t = Track(file_path=file_path, codec=config.CODEC, info=track_info)
        t.play()
    except Exception as e:
        print(e)