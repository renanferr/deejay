from youtube_dl import YoutubeDL
from time import time

def download_track(url, out_file, codec):
    opts = ydl_opts(out_file, codec)
    with YoutubeDL(opts) as ydl:
        ydl.cache.remove()
        info_dict = ydl.extract_info(url, download=False)
        ydl.prepare_filename(info_dict)
        ydl.download([url])
        return info_dict

def ydl_opts(out_file, codec):
    return {
        'format': 'bestaudio/best',
        'outtmpl': out_file,
        'noplaylist': True,
        'continue_dl': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': codec,
            'preferredquality': '192'
        }]
    }