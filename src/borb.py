#!/usr/bin/python3

# This is licensed under the MIT license
# Copyright 2020 Max Suica

import speech
import pyperclip
from sound import play
import text_tools
from pathlib import Path
from conf import *
from cache import with_file_cache

Template = lambda T: lambda A: print(T.format(*A))
PROGRESS_REPORT = Template("\nSegment {}:\n------\n{}")

@with_file_cache
def speak(text):
    """Synthesize and play a speech

    Args:
        text (str): Text to synthesize
        silent: don't play speech
        lazy: play speech after getting all segments

    Returns:
        byte: A byte stream
    """
    print("Synthesizing speech")
    buffers = []
    for seg in text_tools.segment(text):
        PROGRESS_REPORT(seg)
        stream = speech.synth(seg[1])
        buffers.append(stream)
        play(stream)
    # Join buffers into a playable mp3 stream
    buffers = b"".join(buffers)
    return buffers

def stdin():
    return speak(sys.stdin.readlines())

def clip():
    return speak(pyperclip.paste())

if __name__ == "__main__":
    speak("Henlo, I am Borb.")