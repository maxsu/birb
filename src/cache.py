from conf import *
import text_tools
from pathlib import Path
import sound

Template = lambda T: lambda A: print(T.format(*A))
CACHE_REPORT = Template("Playing cached text {}.\nText:\n{}")
CACHE_REPORT2 = Template("Text {}.")

def with_file_cache(_speak):
    """Decorator that adds a file cache layer to our speech engine

    Allows borb to be used for commonly repeated speech
    """
    def wrapped(text):
        id = text_tools.digest(text)
        doc = (id, text)
        root = Path(conf.cache) / id
        mp3 = root.with_suffix(".mp3")
        txt = root.with_suffix(".txt")
        if mp3.exists():
            CACHE_REPORT(doc)
            sound.play(mp3)
            return mp3.read_bytes()
        else:
            CACHE_REPORT2(doc)
            buffer = _speak(text)
            mp3.write_bytes(buffer),
            txt.write_text(text),
    return wrapped