import borb
from pathlib import Path

# Setup
borb.conf.page_size = 10
borb.conf.cache = Path('./test')

# Test
borb.speak('This sentence will be\n spoken in a few chunks')

# Teardown
for x in borb.conf.cache.glob('*.mp3'):
    x.unlink()