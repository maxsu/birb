#!/usr/bin/python3

# This is licensed under the MIT license
# Copyright 2020 Max Suica

import speech
import pyperclip
from Sound import play
import Text
from pathlib import Path
from conf import *
import cache

PROGRESS_REPORT = Text.template("\nSegment {}:\n------\n{}")
CACHE_REPORT = Text.template("Playing text.\nText:\n{}")
SHORT_REPORT = Text.template("Text:\n{}")

def speak(text):
	"""Synthesize and play a speech

	Args:
		text (str): Text to synthesize
		silent: don't play speech
		lazy: play speech after getting all segments

	Returns:
		byte: A byte stream
	"""

	# Preprocess text
	text = Text.clean(text)

	# Play cached speech if possible
	cached_speech = cache.retrieve(text)
	if cached_speech:
		CACHE_REPORT((text,))
		play(cached_speech[1])
		return

	print("Synthesizing speech")
	segments = Text.segment(text, conf.page_size)

	# If speech is short, flush it to disk before play
	# (speed up retries for interrupted speeches)
	if len(segments) == 1:
		text = segments[0][1]
		SHORT_REPORT((text,))
		buffer = speech.synth(text)
		mp3 = cache.store(text, buffer)
		play(mp3)
		return

	buffers = []
	for num, text in segments:
		PROGRESS_REPORT((num, text))
		stream = speech.synth(text)
		buffers.append(stream)
		play(stream)
	buffer = b"".join(buffers)
	cache.store(text, buffer)

def stdin():
	return speak(sys.stdin.readlines())

def clip():
	return speak(pyperclip.paste())

if __name__ == "__main__":
	speak("Henlo, I am Borb.")