# Generated from punto5.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,36,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,4,3,26,8,3,11,3,12,
        3,27,1,4,4,4,31,8,4,11,4,12,4,32,1,4,1,4,0,0,5,1,1,3,2,5,3,7,4,9,
        5,1,0,2,1,0,48,57,3,0,9,10,13,13,32,32,37,0,1,1,0,0,0,0,3,1,0,0,
        0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,1,11,1,0,0,0,3,20,1,0,0,0,
        5,22,1,0,0,0,7,25,1,0,0,0,9,30,1,0,0,0,11,12,5,70,0,0,12,13,5,73,
        0,0,13,14,5,66,0,0,14,15,5,78,0,0,15,16,5,65,0,0,16,17,5,67,0,0,
        17,18,5,67,0,0,18,19,5,73,0,0,19,2,1,0,0,0,20,21,5,40,0,0,21,4,1,
        0,0,0,22,23,5,41,0,0,23,6,1,0,0,0,24,26,7,0,0,0,25,24,1,0,0,0,26,
        27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,8,1,0,0,0,29,31,7,1,0,
        0,30,29,1,0,0,0,31,32,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,34,
        1,0,0,0,34,35,6,4,0,0,35,10,1,0,0,0,3,0,27,32,1,6,0,0
    ]

class punto5Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    INT = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'FIBNACCI'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "INT", "WS" ]

    grammarFileName = "punto5.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


