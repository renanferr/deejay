from youtube_dl import YoutubeDL

url = 'https://www.youtube.com/watch?v=BME88lS6aVY'

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'teste.wav',
    'noplaylist': True,
    'continue_dl': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }]
}

try:
    with YoutubeDL(ydl_opts) as ydl:
        ydl.cache.remove()
        info_dict = ydl.extract_info(url, download=False)
        ydl.prepare_filename(info_dict)
        ydl.download([url])
except Exception as e:
    print(e)