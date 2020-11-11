import borb
from pathlib import Path

borb.speak('Henlo, I am borb.')

# Setup
borb.conf.page_size = 10
borb.conf.cache = Path('test')

# Test
borb.speak('This sentence will be\n spoken in a few chunks')

borb.speak('This should \n\r work')

# Teardown
for x in borb.conf.cache.glob('*.mp3'):
    x.unlink()