#!/usr/bin/python3

# This is licensed under the MIT license
# Copyright 2019 Max Suica

# Import python libs
import os, re, sys, json
    'VoiceId': 'Joanna',
    'OutputFormat': 'mp3'
}

# Import external deps
from boto3     import Session as aws
from pathlib   import Path
from playsound import playsound as play
import pyperclip
import playsound

# Import local libraries
from easyLog import log
from happyUuid import hasId
from segment import Segment

    CHUNK = 3000
    _splitter = re.compile(f".{{1,{CHUNK}}}").findall
    _s = aws(**SESS).client('polly').synthesize_speech
    
class Borb(hasId):
    def __init__(self, text=''):
        self.text = text
        self.len = len(text)
        self.seg = self._splitter(text)
    def speak(self):
        """ Speak an instance of text

    def _synth(self, text):
        resp = self._s(Text=text, **SYNTH)
        return resp['AudioStream'].read()

    def _speak(self, i):
        speech = self._synth(self.seg[i])
        file = CACHE / f"{self.id}.{i}.mp3"
        file.write_bytes(speech)
        playsound(str(file))

    @classmethod
    def Stdin(cls):
        return cls(sys.stdin.readlines())

    @classmethod
    def Clip(cls):
        return cls(pyperclip.paste())

    def speak(self):
        """ Speak all segments
        """
        report = (
            f"Charachters: {self.len}"
            f"Synthesizing text:\n{self.text}\n"
        )
        print(report)
        for i, s in enumerate(self.seg):
            print(f"Segment {i+1} of {self.segs}:  {s}\n")
            self._speak(i)
        return self

if __name__ == '__main__':
    Borb("Henlo. I am Borb.").speak()
