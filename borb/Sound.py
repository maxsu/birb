from playsound import playsound
from pathlib import Path as p
from conf import conf


TMP_BUF = conf.cache / 'tmp.mp3'

def play(resource,):
    if isinstance(resource, p):
        playsound(resource.__str__())
    elif isinstance(resource, bytes):
        TMP_BUF.write_bytes(resource)
        playsound(TMP_BUF.__str__())
        TMP_BUF.unlink()
    else:
        raise NotImplementedError