from playsound import playsound
from pathlib import Path as p
from conf import conf
from random import random

def play(resource,):
	if isinstance(resource, p):
		playsound(resource.__str__())
	elif isinstance(resource, bytes):
		temp_file = conf.cache / "tmp_{}.mp3".format(str(random())[-6:])
		temp_file.write_bytes(resource)
		playsound(temp_file.__str__())
		temp_file.unlink()
	else:
		raise NotImplementedError