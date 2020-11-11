import toml
from pathlib import Path as p
from munch import Munch


try:
    conf = toml.load("conf.toml", _dict=Munch)
    credentials = toml.load("credentials.toml", _dict=Munch)

except FileNotFoundError as e:
    try:
        conf = toml.load("../conf.toml", _dict=Munch)
        credentials = toml.load("../credentials.toml", _dict=Munch)
    except:
        sys.exit('Could not find configuration.')


if conf.cache:
    conf.cache = p.home() / conf.cache

try:
    conf.session.update(credentials.session)
except:
    sys.exist('Could not load credentials.')