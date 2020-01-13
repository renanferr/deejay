from playback import Track
from ytdl import download_track
from config import config
from time import time
from utils import clear_dir
# from socketio-server import app
import os
import eventlet
from http2_server import H2Server, H2Protocol
from ws_server import WebsocketServer

url = 'https://www.youtube.com/watch?v=POH14-HMGFc'


if __name__ == '__main__':
    # clear_dir(dir_path=config.TMP_DIR)
    s = WebsocketServer()
    s.start()
    # h2server = H2Server(H2Protocol, enable_ssl=False)
    # h2server.start()
    # eventlet.wsgi.server(eventlet.listen(('', 5000)), app)