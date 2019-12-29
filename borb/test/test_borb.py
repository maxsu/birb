#!/usr/bin/python3
from unittest import TestCase, main
from pathlib import Path
import pyperclip

import sys
sys.path.append(str(Path('borb').resolve()))

import borb

class TestBorb(TestCase):
    def test_shortstring(self):
        borb.speak("Test 1")

    def test_empylines(self):
        testString = """line 1

            line 2
            """
        borb.speak(testString)

    def test_emptyinit(self):
        # Test empty init
        borb.speak()

    def test_clipboard(self):
        # Test clipboard
        test = "test clipboard"
        pyperclip.copy(test)
        borb.clip()

    def test_mediumstring(self):
        testString = """line 1
                line 2
                line 3"""
        borb.speak(testString)

    def test_whitepspace(self):
        # Test empty string
        borb.speak("    ")

    def test_carriagereturn(self):
        borb.speak('\r')

    def test_tripldoublequote(self):
        borb.speak('"""')

    def test_problemstrings(self):
        borb.speak("*   *")


main()
