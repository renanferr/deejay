from playback import Track
from ytdl import download_track
from config import config
from time import time
from utils import clear_dir
from server import app
import os
import eventlet

url = 'https://www.youtube.com/watch?v=POH14-HMGFc'


if __name__ == '__main__':
    clear_dir(dir_path=config.TMP_DIR)
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)