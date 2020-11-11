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


# clean('test \r test') = 'test \n test'
# 'The CHERRY_PICK_HEAD ref is set to point at the commit that introduced the change that is difficult to apply.\r\n\r\nPaths in which the change applied cleanly are updated both in the index file and in your working tree.\r\n\r\nFor conflicting paths, the index file records up to three versions, as described in the "TRUE MERGE" section of git-merge(1). The working tree files will include a description of the conflict bracketed by the usual conflict markers <<<<<<< and >>>>>>>.\r\n\r\nNo other modifications are made.\r\n\r\nSee git-merge(1) for some hints on resolving such conflicts.'"
# 'The CHERRY_PICK_HEAD ref is set to point at the commit that introduced the change that is difficult to apply.\nPaths in which the change applied cleanly are updated both in the index file and in your working tree.\nFor conflicting paths, the index file records up to three versions, as described in the "TRUE MERGE" section of git-merge(1). The working tree files will include a description of the conflict bracketed by the usual conflict markers <<<<<<< and >>>>>>>.\nNo other modifications are made.\nSee git-merge(1) for some hints on resolving such conflicts.'