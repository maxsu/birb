from playsound import playsound
from pathlib import Path as p
from conf import conf


TMP_BUF = p(conf.cache) / 'tmp.mp3'

def play(byte_stream):
    TMP_BUF.write_bytes(byte_stream)
    playsound(TMP_BUF.__str__())
    TMP_BUF.unlink()