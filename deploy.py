import sys
sys.path.append('borb')

import toml
from pathlib import Path as p
from munch import Munch
from itertools import chain
from pathlib import Path

DELETE_REPORT = "DELETING: {}.".format
COPY_REPORT = "COPYING: {}".format


conf = toml.load("pyproject.toml", _dict=Munch).deploy

root = Path()
src = root / conf.src
target = Path.home() / conf.target

# Clean old files
files = chain(
    target.glob('*.py'),
    target.glob('*.ahk'),
    target.glob('*.toml'))

for file in files:
    print(DELETE_REPORT(file))
    file.unlink()


# Push files
# Clean old files
files = chain(
    src.glob('*.py'),
    root.glob('*.ahk'),
    root.glob('*.toml'))

for file in files:
    print(COPY_REPORT(file))
    destination =  target / file.name
    destination.write_text(file.read_text())

