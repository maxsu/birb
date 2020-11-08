import Text
from conf import *

def _with_root(id, suffix):
    return (conf.cache / id).with_suffix(suffix)

def retrieve(text):
    id = Text.speech_id(text)
    mp3 = _with_root(id, '.mp3')
    if mp3.exists():
        return (id, mp3)
    else:
        return False

def store(text, buffer):
    id = Text.speech_id(text)
    txt = _with_root(id, '.txt')
    mp3 = _with_root(id, '.mp3')
    txt.write_text(text)
    mp3.write_bytes(buffer)
    return mp3


if not conf.cache:
    retrieve = store = lambda: False