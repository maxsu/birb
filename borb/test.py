#  Copyright (C) 2019  Mars Industrial - All Rights Reserved
#  Unauthorized copying of this file via any medium is prohibited.
#  See 'COPYRIGHT' which is part of this source code package
#  Written by Max Suica <max.suica@gmail.com> October, 2019

import pyperclip
import borb
from nose2.tools import such, params

with such.A('Amazing Speech Engine') as BORB:

    @BORB.should('speak small strings')
    @params("", "test 1", "line 1 \n line 2", "")
    def test_small_string(value):
        assert borb.speak(value)

    @BORB.should('raise for no text param')
    def test_empty(value):
        borb.speak()

    @BORB.should('speak clipboard contents')
    @params("test clipboard a", "test clipboard b")
    def test_clipboard(value):
        pyperclip.copy(value)
        borb.clip()

    @BORB.should('speak medium strings')
    def test_mediumstring(value):
        testString = """line 1
                line 2
                line 3"""
        borb.speak(testString)

    @BORB.should('Say nothing for empty strings, whitespace, or punctuation')
    @params("", "        ", "*   *", " , . . . , . . ..", "\"\"\"\"", " \r ")
    def test_whitepspace(value):
        borb.speak(value)

with such.A('Decent Text Normalizing Engine') as SEGMENT:
    @SEGMENT.should('Segment the empty string into itself')
    def test_empty_string(case):
        assert len(borb.segment("")) == 1

    @SEGMENT.should('Do these examples in this way')
    @params(
        ('abc', ["ab", "c", ""]),
        ("123", ["12", "3", ""]),
        ("abcdefghijkl", ["ab", "cd", "ef", "gh", "ij", "kl", ""])
    )
    def test_examples(v):
        assert borb.segment(v[0], chunk=2) == v[1]
