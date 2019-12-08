#!/usr/bin/python3

# This is licensed under the MIT license
# Copyright 2019 Max Suica

# Import python libs
import os, re, sys, json

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

import json

conf = 'borb/borbConfig.json'
opt = json.loads(Path(conf).resolve().read_text())

class Borb(hasId):

    def __init__(self, text=''):
        self.polly = aws(**opt['session']).client('polly').synthesize_speech
        self.text = text
        self.seg = Segment.normalize(text)
        
    def speak(self):
        """ Speak an instance of text

            Play sound directly
            Cache text in cache/id.i.mp3
        """
        text = self.text
        seg = self.seg
        segs = len(seg)
        
        log("Charachters: {}\n" "Synthesizing text:\n{}", len(text), text)
        
        # Process segments
        for i, s in enumerate(seg):
            log("\nSegment {} of {}:  {}", i+1, segs, s)
            # Get segment from synth
            speech = self.polly(Text=s, **opt['synth'])['AudioStream'].read()
            log("Response bytes: {}", len(speech))

            # Write segment to cache
            file = Path(opt['cache']) / f"{self.id}.{i}.mp3"
            file.write_bytes(speech)
            log("Wrote file: {}", file)

            # Speak segment
            log("Playing segment.")
            play(str(file))

        return self

    @classmethod
    def Stdin(cls):
        return cls(sys.stdin.readlines())

    @classmethod
    def Clip(cls):
        return cls(pyperclip.paste())

if __name__ == '__main__':
    Borb("Henlo. I am Borb.").speak()
