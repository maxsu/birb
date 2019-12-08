#!/usr/bin/python3
import os
import re
import sys
import uuid
from boto3 import Session as aws
from pathlib import Path
from playsound import playsound
import pyperclip

# This is licensed under the MIT license
# Copyright 2019 Max Suica

SYNTH = {
    'Engine': 'neural',
    'VoiceId': 'Joanna',
    'OutputFormat': 'mp3'
}

SESS = {
    'profile_name': 'default',
    'region_name': 'us-west-2'
}

class Borb:

    CHUNK = 3000
    _splitter = re.compile(f".{{1,{CHUNK}}}").findall
    _s = aws(**SESS).client('polly').synthesize_speech
    
    def __init__(self, text=''):
        self.text = text
        self.len = len(text)
        self.seg = self._splitter(text)
        self.segs = len(self.seg)
        self.id = uuid.uuid4().hex

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
