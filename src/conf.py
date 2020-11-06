import toml
from munch import Munch

conf = toml.load("conf.toml", _dict=Munch)