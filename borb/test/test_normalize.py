#  Copyright (C) 2019  Mars Industrial - All Rights Reserved
#  Unauthorized copying of this file via any medium is prohibited.
#  See 'COPYRIGHT' which is part of this source code package
#  Written by Max Suica <max.suica@gmail.com> October, 2019

from pathlib import Path
import sys
from unittest import TestCase, main

sys.path.append(str(Path('borb').resolve()))

import borb


class TestNormalize(TestCase):

    def test_defaultVal(self):
        self.assertEqual(
            len(list(borb.normalize(""))), 
            1
        )

    def test_functionalInit(self):
        val = borb.normalize("abc", 2)
        val2 = borb.normalize("123", 2)
        val3 = borb.normalize("abcdefghijkl", 2)

        self.assertEqual(list(val), ["ab", "c", ""])
        self.assertEqual(list(val2), ["12", "3", ""])
        self.assertEqual(list(val3), ["ab", "cd", "ef", 
                                      "gh", "ij", "kl", ""])


main()
