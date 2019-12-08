from pathlib import Path

import sys
sys.path.append(
    Path('borb').resolve().__str__()
)

from borb import Borb

Borb.Clip().speak()
