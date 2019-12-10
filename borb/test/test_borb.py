#!/usr/bin/python3
from unittest import TestCase, main
from pathlib import Path
import pyperclip

import sys
sys.path.append(str(Path('borb').resolve()))
from borb import Borb


class TestBorb(TestCase):
    def test_shortstring(self):
        Borb("Test 1").speak()

    def test_empylines(self):
        testString = """line 1

            line 2
            """
        Borb(testString).speak()

    def test_emptyinit(self):
        # Test empty init
        Borb().speak()

    def test_clipboard(self):
        # Test clipboard
        test = "test clipboard"
        pyperclip.copy(test)
        b1 = Borb.Clip().speak()
        self.assertEqual(b1.text, test)

    def test_mediumstring(self):
        testString = """line 1
                line 2
                line 3"""
        b2 = Borb(testString).speak()
        self.assertEqual(len(b2.seg), 1)

    def test_whitepspace(self):
        # Test empty string
        Borb("    ").speak()

    def test_carriagereturn(self):
        Borb('\r').speak()

    def test_tripldoublequote(self):
        Borb('"""').speak()

    def test_problemstrings(self):
        Borb("*   *").speak()


main()
