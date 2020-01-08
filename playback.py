import pydub
from pydub.playback import play as p

class Track():
    def __init__(self, file_path, codec, info):
        self.file_path = file_path
        self.info = info
        self.codec = codec
        self._data = pydub.AudioSegment.from_file(self.file_path, format=self.codec)
    
    def play(self):
        print('playing track...')
        return p(self._data)