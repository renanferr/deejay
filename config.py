import os

defaults = {
    'CODEC': 'mp3',
    'TMP_DIR': './tmp'
}

class Config():
    def __init__(self):
        for k in defaults:
            if os.getenv(k) is not None:
                self.__setattr__(k, os.getenv(k))
            else:
                self.__setattr__(k, defaults.get(k))
        
        self.OUT_TMP = os.path.join(self.TMP_DIR, '%(id)s.%(ext)s')

config = Config()
