#!/usr/bin/python3

# This is licensed under the MIT license
# Copyright 2019 Max Suica

import json
import re
import sys
import uuid

from boto3 import Session as aws
from pathlib import Path
from playsound import playsound as play
import pyperclip

opt = json.loads(Path('borbConfig.json').read_text())


def normalize(text, chunk=3000, word=False):
    """ Split text into uniform chunks

        Uses existing line breaks
        Todo: Linebreaks > Word-Chunk > Chunk
        Avoid breaking strings at words  existing line breaks

        chunk: int  chunk size
    """

    regex = f".{{1,{chunk}}}"
    chop = re.compile(regex).findall
    result = ""

    for line in text.splitlines():
        if len(line) + len(result) < chunk:
            result += "\n" + line
        else:
            if len(line) > chunk:
                result += "\n" + line
                yield from chop(result)
                result = ""
            else:
                yield result
                result = line
    yield result


def speak(text=""):
    """ Speak an arbitrary length of text
    """

    client = aws(**opt['session']).client('polly')
    id = uuid.uuid4().hex
    seg = list(normalize(text))
    segs = len(seg)

    print("Synthesizing speech")

    for i, s in enumerate(seg):

        speech = client.synthesize_speech(
            Text=s,
            **opt['synth']
        )['AudioStream'].read()

        print(f"\nSegment {i+1} of {segs}:  {s}")

        if len(speech) >= 512:
            file = Path(opt['cache']) / f"{id}.{i}.mp3"
            file.write_bytes(speech)

            print(f"Wrote file (kbytes): {file} ({len(speech) / 1024.0} kb)")

            # if playing, wait to stop; play async
            play(str(file))
            # Continue; fetch next segment while playing


def stdin():
    return speak(sys.stdin.readlines())


def clip():
    return speak(pyperclip.paste())


if __name__ == '__main__':
    speak("Henlo. I am Borb. I am happy to help you read things!")
