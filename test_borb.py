#!/usr/bin/python3
from unittest import TestCase, main
from pathlib import Path
import pyperclip
from borb import Borb


if __name__ == '__main__':

    testString = """testline 1
    testline 2
    testline 3"""

    class TestBorb(TestCase):
        def test_shortstring(self):
            instance = Borb("Test 1")
            instance._speak = (
                lambda _self, i: self.assertEqual(i, 0)).__get__(instance)
            instance.speak()

        def test_clipboard(self):
            # Test clipboard
            test = "test 1"
            pyperclip.copy(test)
            b1 = Borb.Clip().speak()
            self.assertEqual(b1.text, test)

        def test_mediumstring(self):
            b2 = Borb("test 2:" + testString).speak()
            self.assertEqual(b2.segs, 3)
        def test_whitepspace(self):
            # Test empty string
            Borb("    ").speak()

        def test_emptyinit(self):
            # Test empty init
            Borb().speak()

main()
