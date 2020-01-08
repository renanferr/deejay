import os

defaults = {
    'CODEC': 'mp3',
    'TMP_DIR': './tmp'
}

class Config():
    def __init__(self):
        for k in defaults:
            self.__setattr__(k, defaults.get(k))
        self.OUT_TMP = os.path.join(self.TMP_DIR, '%(id)s.%(ext)s')

config = Config()
