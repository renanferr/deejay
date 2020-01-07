from youtube_dl import YoutubeDL
from contextlib import redirect_stdout
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

def copy_filelike_to_filelike(src, dst, bufsize=16384):
    while True:
        buf = src.read(bufsize)
        print(buf)
        if not buf:
            break
        dst.write(buf)

url = 'https://www.youtube.com/watch?v=BME88lS6aVY'

TMP_PREFIX='./tmp/'
PREFERRED_CODEC='mp3'
FILENAME='{}tmp.%(ext)s'.format(TMP_PREFIX)
DEST_FILE='{}tmp.{}'.format(TMP_PREFIX, PREFERRED_CODEC)

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': FILENAME,
    'noplaylist': True,
    # 'quiet': True,
    'continue_dl': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': PREFERRED_CODEC,
        'preferredquality': '192'
    }]
}


try:
    with YoutubeDL(ydl_opts) as ydl:
        ydl.cache.remove()
        info_dict = ydl.extract_info(url, download=False)
        ydl.prepare_filename(info_dict)
        # print(info_dict['ext'])
        ydl.download([url])
        # with open(FILENAME, 'rb') as file:
        song = AudioSegment.from_file(DEST_FILE, format=PREFERRED_CODEC)
        # mp3_file = '{}.mp3'.format(FILENAME)
        # song.export(mp3_file, format='mp3')
        # play(AudioSegment.from_mp3(mp3_file, format='mp3'))
        play(song)
except Exception as e:
    print(e)