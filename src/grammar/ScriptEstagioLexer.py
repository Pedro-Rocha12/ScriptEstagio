# Generated from grammar/ScriptEstagio.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,26,220,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,
        5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,
        11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,
        14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,1,
        15,1,15,1,15,1,16,1,16,1,16,1,16,3,16,150,8,16,1,17,1,17,1,18,1,
        18,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,20,1,20,3,20,184,8,20,1,21,4,21,187,8,21,11,21,12,21,188,1,
        22,4,22,192,8,22,11,22,12,22,193,1,23,1,23,5,23,198,8,23,10,23,12,
        23,201,9,23,1,23,1,23,1,24,4,24,206,8,24,11,24,12,24,207,1,24,1,
        24,1,25,1,25,5,25,214,8,25,10,25,12,25,217,9,25,1,25,1,25,1,199,
        0,26,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,
        13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,
        24,49,25,51,26,1,0,4,3,0,65,90,97,122,192,255,1,0,48,57,3,0,9,10,
        13,13,32,32,2,0,10,10,13,13,226,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,
        0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,
        0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,
        0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,
        0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,
        0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,1,53,1,0,0,0,3,61,1,0,0,
        0,5,66,1,0,0,0,7,68,1,0,0,0,9,74,1,0,0,0,11,84,1,0,0,0,13,86,1,0,
        0,0,15,88,1,0,0,0,17,98,1,0,0,0,19,101,1,0,0,0,21,111,1,0,0,0,23,
        114,1,0,0,0,25,117,1,0,0,0,27,127,1,0,0,0,29,129,1,0,0,0,31,138,
        1,0,0,0,33,149,1,0,0,0,35,151,1,0,0,0,37,153,1,0,0,0,39,155,1,0,
        0,0,41,183,1,0,0,0,43,186,1,0,0,0,45,191,1,0,0,0,47,195,1,0,0,0,
        49,205,1,0,0,0,51,211,1,0,0,0,53,54,5,97,0,0,54,55,5,103,0,0,55,
        56,5,101,0,0,56,57,5,110,0,0,57,58,5,100,0,0,58,59,5,97,0,0,59,60,
        5,114,0,0,60,2,1,0,0,0,61,62,5,116,0,0,62,63,5,111,0,0,63,64,5,100,
        0,0,64,65,5,97,0,0,65,4,1,0,0,0,66,67,5,58,0,0,67,6,1,0,0,0,68,69,
        5,103,0,0,69,70,5,101,0,0,70,71,5,114,0,0,71,72,5,97,0,0,72,73,5,
        114,0,0,73,8,1,0,0,0,74,75,5,114,0,0,75,76,5,101,0,0,76,77,5,108,
        0,0,77,78,5,97,0,0,78,79,5,116,0,0,79,80,5,111,0,0,80,81,5,114,0,
        0,81,82,5,105,0,0,82,83,5,111,0,0,83,10,1,0,0,0,84,85,5,123,0,0,
        85,12,1,0,0,0,86,87,5,125,0,0,87,14,1,0,0,0,88,89,5,114,0,0,89,90,
        5,101,0,0,90,91,5,103,0,0,91,92,5,105,0,0,92,93,5,115,0,0,93,94,
        5,116,0,0,94,95,5,114,0,0,95,96,5,97,0,0,96,97,5,114,0,0,97,16,1,
        0,0,0,98,99,5,101,0,0,99,100,5,109,0,0,100,18,1,0,0,0,101,102,5,
        100,0,0,102,103,5,97,0,0,103,104,5,116,0,0,104,105,5,97,0,0,105,
        106,5,72,0,0,106,107,5,111,0,0,107,108,5,114,0,0,108,109,5,97,0,
        0,109,110,5,115,0,0,110,20,1,0,0,0,111,112,5,115,0,0,112,113,5,101,
        0,0,113,22,1,0,0,0,114,115,5,61,0,0,115,116,5,61,0,0,116,24,1,0,
        0,0,117,118,5,110,0,0,118,119,5,111,0,0,119,120,5,116,0,0,120,121,
        5,105,0,0,121,122,5,102,0,0,122,123,5,105,0,0,123,124,5,99,0,0,124,
        125,5,97,0,0,125,126,5,114,0,0,126,26,1,0,0,0,127,128,5,59,0,0,128,
        28,1,0,0,0,129,130,5,102,0,0,130,131,5,111,0,0,131,132,5,114,0,0,
        132,133,5,109,0,0,133,134,5,97,0,0,134,135,5,116,0,0,135,136,5,111,
        0,0,136,137,5,58,0,0,137,30,1,0,0,0,138,139,5,104,0,0,139,140,5,
        111,0,0,140,141,5,114,0,0,141,142,5,97,0,0,142,143,5,115,0,0,143,
        144,5,59,0,0,144,32,1,0,0,0,145,146,5,97,0,0,146,150,5,115,0,0,147,
        148,5,224,0,0,148,150,5,115,0,0,149,145,1,0,0,0,149,147,1,0,0,0,
        150,34,1,0,0,0,151,152,5,224,0,0,152,36,1,0,0,0,153,154,5,45,0,0,
        154,38,1,0,0,0,155,156,5,95,0,0,156,40,1,0,0,0,157,158,5,111,0,0,
        158,159,5,114,0,0,159,160,5,105,0,0,160,161,5,103,0,0,161,162,5,
        101,0,0,162,163,5,109,0,0,163,164,5,45,0,0,164,165,5,100,0,0,165,
        166,5,97,0,0,166,167,5,100,0,0,167,168,5,111,0,0,168,169,5,115,0,
        0,169,184,5,58,0,0,170,171,5,111,0,0,171,172,5,114,0,0,172,173,5,
        105,0,0,173,174,5,103,0,0,174,175,5,101,0,0,175,176,5,109,0,0,176,
        177,5,95,0,0,177,178,5,100,0,0,178,179,5,97,0,0,179,180,5,100,0,
        0,180,181,5,111,0,0,181,182,5,115,0,0,182,184,5,58,0,0,183,157,1,
        0,0,0,183,170,1,0,0,0,184,42,1,0,0,0,185,187,7,0,0,0,186,185,1,0,
        0,0,187,188,1,0,0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,44,1,0,0,
        0,190,192,7,1,0,0,191,190,1,0,0,0,192,193,1,0,0,0,193,191,1,0,0,
        0,193,194,1,0,0,0,194,46,1,0,0,0,195,199,5,34,0,0,196,198,9,0,0,
        0,197,196,1,0,0,0,198,201,1,0,0,0,199,200,1,0,0,0,199,197,1,0,0,
        0,200,202,1,0,0,0,201,199,1,0,0,0,202,203,5,34,0,0,203,48,1,0,0,
        0,204,206,7,2,0,0,205,204,1,0,0,0,206,207,1,0,0,0,207,205,1,0,0,
        0,207,208,1,0,0,0,208,209,1,0,0,0,209,210,6,24,0,0,210,50,1,0,0,
        0,211,215,5,35,0,0,212,214,8,3,0,0,213,212,1,0,0,0,214,217,1,0,0,
        0,215,213,1,0,0,0,215,216,1,0,0,0,216,218,1,0,0,0,217,215,1,0,0,
        0,218,219,6,25,0,0,219,52,1,0,0,0,8,0,149,183,188,193,199,207,215,
        1,6,0,0
    ]

class ScriptEstagioLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    AS = 17
    A = 18
    HIFEN = 19
    UNDERSCORE = 20
    ORIGEM_DADOS = 21
    PALAVRA = 22
    NUMERO = 23
    CADEIA = 24
    ESPACO = 25
    COMENTARIO = 26

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'agendar'", "'toda'", "':'", "'gerar'", "'relatorio'", "'{'", 
            "'}'", "'registrar'", "'em'", "'dataHoras'", "'se'", "'=='", 
            "'notificar'", "';'", "'formato:'", "'horas;'", "'\\u00E0'", 
            "'-'", "'_'" ]

    symbolicNames = [ "<INVALID>",
            "AS", "A", "HIFEN", "UNDERSCORE", "ORIGEM_DADOS", "PALAVRA", 
            "NUMERO", "CADEIA", "ESPACO", "COMENTARIO" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "AS", "A", "HIFEN", "UNDERSCORE", "ORIGEM_DADOS", 
                  "PALAVRA", "NUMERO", "CADEIA", "ESPACO", "COMENTARIO" ]

    grammarFileName = "ScriptEstagio.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


