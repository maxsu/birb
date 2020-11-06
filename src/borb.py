#!/usr/bin/python3

# This is licensed under the MIT license
# Copyright 2020 Max Suica

import polly
import pyperclip
from sound import play
from text import segment

def speak(text):
        segments = segment(text)
        print('Synthesizing speech')
        for num, text in segments:
            print(f'Segment {num}: {text}')
            stream = polly.synth(text)
            play(stream)

def stdin():
    return speak(sys.stdin.readlines())

def clip():
    return speak(pyperclip.paste())

if __name__ == "__main__":
    speak("Henlo, I am Borb.")