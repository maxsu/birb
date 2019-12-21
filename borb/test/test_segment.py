#  Copyright (C) 2019  Mars Industrial - All Rights Reserved
#  Unauthorized copying of this file via any medium is prohibited.
#  See 'COPYRIGHT' which is part of this source code package
#  Written by Max Suica <max.suica@gmail.com> October, 2019

from pathlib import Path
import sys
from unittest import TestCase, main

sys.path.append(str(Path('borb').resolve()))

from funtools import _Res
from segment import Segment



class TestSegment(TestCase):

    def test_defaultVal(self):
        self.assertEqual(len(_Res()), 0)

    def test_functionalInit(self):
        val = Segment.normalize("abc", 2).data
        val2 = Segment.normalize("123", 2).data

        print(val, val2)
        self.assertEqual(val, ["", "ab", "c"])
        self.assertEqual(val2, ["", "12", "3"])

main()
