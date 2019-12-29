from pathlib import Path

import sys
sys.path.append(
    Path('borb').resolve().__str__()
)

import borb

borb.clip()