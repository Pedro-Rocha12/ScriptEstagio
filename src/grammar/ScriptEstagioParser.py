# Generated from grammar/ScriptEstagio.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,102,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,
        5,1,5,4,5,61,8,5,11,5,12,5,62,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,4,
        6,73,8,6,11,6,12,6,74,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,
        7,87,8,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,
        1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,0,99,0,23,1,0,0,0,2,33,
        1,0,0,0,4,35,1,0,0,0,6,44,1,0,0,0,8,52,1,0,0,0,10,57,1,0,0,0,12,
        66,1,0,0,0,14,78,1,0,0,0,16,88,1,0,0,0,18,92,1,0,0,0,20,96,1,0,0,
        0,22,24,3,2,1,0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,
        1,0,0,0,26,1,1,0,0,0,27,34,3,4,2,0,28,34,3,6,3,0,29,34,3,8,4,0,30,
        34,3,10,5,0,31,34,3,12,6,0,32,34,3,14,7,0,33,27,1,0,0,0,33,28,1,
        0,0,0,33,29,1,0,0,0,33,30,1,0,0,0,33,31,1,0,0,0,33,32,1,0,0,0,34,
        3,1,0,0,0,35,36,5,1,0,0,36,37,5,24,0,0,37,38,5,2,0,0,38,39,5,22,
        0,0,39,40,5,17,0,0,40,41,5,23,0,0,41,42,5,3,0,0,42,43,5,23,0,0,43,
        5,1,0,0,0,44,45,5,4,0,0,45,46,5,5,0,0,46,47,5,24,0,0,47,48,5,6,0,
        0,48,49,3,16,8,0,49,50,3,18,9,0,50,51,5,7,0,0,51,7,1,0,0,0,52,53,
        5,8,0,0,53,54,5,24,0,0,54,55,5,9,0,0,55,56,5,24,0,0,56,9,1,0,0,0,
        57,58,5,10,0,0,58,60,5,6,0,0,59,61,3,20,10,0,60,59,1,0,0,0,61,62,
        1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,65,5,7,0,0,
        65,11,1,0,0,0,66,67,5,11,0,0,67,68,5,22,0,0,68,69,5,12,0,0,69,70,
        5,24,0,0,70,72,5,6,0,0,71,73,3,2,1,0,72,71,1,0,0,0,73,74,1,0,0,0,
        74,72,1,0,0,0,74,75,1,0,0,0,75,76,1,0,0,0,76,77,5,7,0,0,77,13,1,
        0,0,0,78,79,5,13,0,0,79,86,5,24,0,0,80,81,5,9,0,0,81,87,5,24,0,0,
        82,83,5,17,0,0,83,84,5,23,0,0,84,85,5,3,0,0,85,87,5,23,0,0,86,80,
        1,0,0,0,86,82,1,0,0,0,87,15,1,0,0,0,88,89,5,21,0,0,89,90,5,24,0,
        0,90,91,5,14,0,0,91,17,1,0,0,0,92,93,5,15,0,0,93,94,5,24,0,0,94,
        95,5,14,0,0,95,19,1,0,0,0,96,97,5,24,0,0,97,98,5,3,0,0,98,99,5,23,
        0,0,99,100,5,16,0,0,100,21,1,0,0,0,5,25,33,62,74,86
    ]

class ScriptEstagioParser ( Parser ):

    grammarFileName = "ScriptEstagio.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'agendar'", "'toda'", "':'", "'gerar'", 
                     "'relatorio'", "'{'", "'}'", "'registrar'", "'em'", 
                     "'dataHoras'", "'se'", "'=='", "'notificar'", "';'", 
                     "'formato:'", "'horas;'", "<INVALID>", "'\\u00E0'", 
                     "'-'", "'_'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "AS", "A", "HIFEN", "UNDERSCORE", "ORIGEM_DADOS", 
                      "PALAVRA", "NUMERO", "CADEIA", "ESPACO", "COMENTARIO" ]

    RULE_script = 0
    RULE_comando = 1
    RULE_agendamento = 2
    RULE_geracaoRelatorio = 3
    RULE_registro = 4
    RULE_logTrabalho = 5
    RULE_tarefaCondicional = 6
    RULE_notificacao = 7
    RULE_origemDados = 8
    RULE_formato = 9
    RULE_dataHoras = 10

    ruleNames =  [ "script", "comando", "agendamento", "geracaoRelatorio", 
                   "registro", "logTrabalho", "tarefaCondicional", "notificacao", 
                   "origemDados", "formato", "dataHoras" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    AS=17
    A=18
    HIFEN=19
    UNDERSCORE=20
    ORIGEM_DADOS=21
    PALAVRA=22
    NUMERO=23
    CADEIA=24
    ESPACO=25
    COMENTARIO=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScriptEstagioParser.ComandoContext)
            else:
                return self.getTypedRuleContext(ScriptEstagioParser.ComandoContext,i)


        def getRuleIndex(self):
            return ScriptEstagioParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)




    def script(self):

        localctx = ScriptEstagioParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.comando()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 11538) != 0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def agendamento(self):
            return self.getTypedRuleContext(ScriptEstagioParser.AgendamentoContext,0)


        def geracaoRelatorio(self):
            return self.getTypedRuleContext(ScriptEstagioParser.GeracaoRelatorioContext,0)


        def registro(self):
            return self.getTypedRuleContext(ScriptEstagioParser.RegistroContext,0)


        def logTrabalho(self):
            return self.getTypedRuleContext(ScriptEstagioParser.LogTrabalhoContext,0)


        def tarefaCondicional(self):
            return self.getTypedRuleContext(ScriptEstagioParser.TarefaCondicionalContext,0)


        def notificacao(self):
            return self.getTypedRuleContext(ScriptEstagioParser.NotificacaoContext,0)


        def getRuleIndex(self):
            return ScriptEstagioParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = ScriptEstagioParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_comando)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.agendamento()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.geracaoRelatorio()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.registro()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.logTrabalho()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 5)
                self.state = 31
                self.tarefaCondicional()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 32
                self.notificacao()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgendamentoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CADEIA(self):
            return self.getToken(ScriptEstagioParser.CADEIA, 0)

        def PALAVRA(self):
            return self.getToken(ScriptEstagioParser.PALAVRA, 0)

        def AS(self):
            return self.getToken(ScriptEstagioParser.AS, 0)

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(ScriptEstagioParser.NUMERO)
            else:
                return self.getToken(ScriptEstagioParser.NUMERO, i)

        def getRuleIndex(self):
            return ScriptEstagioParser.RULE_agendamento

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgendamento" ):
                listener.enterAgendamento(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgendamento" ):
                listener.exitAgendamento(self)




    def agendamento(self):

        localctx = ScriptEstagioParser.AgendamentoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_agendamento)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(ScriptEstagioParser.T__0)
            self.state = 36
            self.match(ScriptEstagioParser.CADEIA)
            self.state = 37
            self.match(ScriptEstagioParser.T__1)
            self.state = 38
            self.match(ScriptEstagioParser.PALAVRA)
            self.state = 39
            self.match(ScriptEstagioParser.AS)
            self.state = 40
            self.match(ScriptEstagioParser.NUMERO)
            self.state = 41
            self.match(ScriptEstagioParser.T__2)
            self.state = 42
            self.match(ScriptEstagioParser.NUMERO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GeracaoRelatorioContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CADEIA(self):
            return self.getToken(ScriptEstagioParser.CADEIA, 0)

        def origemDados(self):
            return self.getTypedRuleContext(ScriptEstagioParser.OrigemDadosContext,0)


        def formato(self):
            return self.getTypedRuleContext(ScriptEstagioParser.FormatoContext,0)


        def getRuleIndex(self):
            return ScriptEstagioParser.RULE_geracaoRelatorio

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeracaoRelatorio" ):
                listener.enterGeracaoRelatorio(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeracaoRelatorio" ):
                listener.exitGeracaoRelatorio(self)




    def geracaoRelatorio(self):

        localctx = ScriptEstagioParser.GeracaoRelatorioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_geracaoRelatorio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(ScriptEstagioParser.T__3)
            self.state = 45
            self.match(ScriptEstagioParser.T__4)
            self.state = 46
            self.match(ScriptEstagioParser.CADEIA)
            self.state = 47
            self.match(ScriptEstagioParser.T__5)
            self.state = 48
            self.origemDados()
            self.state = 49
            self.formato()
            self.state = 50
            self.match(ScriptEstagioParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegistroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CADEIA(self, i:int=None):
            if i is None:
                return self.getTokens(ScriptEstagioParser.CADEIA)
            else:
                return self.getToken(ScriptEstagioParser.CADEIA, i)

        def getRuleIndex(self):
            return ScriptEstagioParser.RULE_registro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegistro" ):
                listener.enterRegistro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegistro" ):
                listener.exitRegistro(self)




    def registro(self):

        localctx = ScriptEstagioParser.RegistroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_registro)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(ScriptEstagioParser.T__7)
            self.state = 53
            self.match(ScriptEstagioParser.CADEIA)
            self.state = 54
            self.match(ScriptEstagioParser.T__8)
            self.state = 55
            self.match(ScriptEstagioParser.CADEIA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogTrabalhoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dataHoras(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScriptEstagioParser.DataHorasContext)
            else:
                return self.getTypedRuleContext(ScriptEstagioParser.DataHorasContext,i)


        def getRuleIndex(self):
            return ScriptEstagioParser.RULE_logTrabalho

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogTrabalho" ):
                listener.enterLogTrabalho(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogTrabalho" ):
                listener.exitLogTrabalho(self)




    def logTrabalho(self):

        localctx = ScriptEstagioParser.LogTrabalhoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_logTrabalho)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(ScriptEstagioParser.T__9)
            self.state = 58
            self.match(ScriptEstagioParser.T__5)
            self.state = 60 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 59
                self.dataHoras()
                self.state = 62 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==24):
                    break

            self.state = 64
            self.match(ScriptEstagioParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TarefaCondicionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PALAVRA(self):
            return self.getToken(ScriptEstagioParser.PALAVRA, 0)

        def CADEIA(self):
            return self.getToken(ScriptEstagioParser.CADEIA, 0)

        def comando(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScriptEstagioParser.ComandoContext)
            else:
                return self.getTypedRuleContext(ScriptEstagioParser.ComandoContext,i)


        def getRuleIndex(self):
            return ScriptEstagioParser.RULE_tarefaCondicional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTarefaCondicional" ):
                listener.enterTarefaCondicional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTarefaCondicional" ):
                listener.exitTarefaCondicional(self)




    def tarefaCondicional(self):

        localctx = ScriptEstagioParser.TarefaCondicionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tarefaCondicional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ScriptEstagioParser.T__10)
            self.state = 67
            self.match(ScriptEstagioParser.PALAVRA)
            self.state = 68
            self.match(ScriptEstagioParser.T__11)
            self.state = 69
            self.match(ScriptEstagioParser.CADEIA)
            self.state = 70
            self.match(ScriptEstagioParser.T__5)
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                self.comando()
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 11538) != 0):
                    break

            self.state = 76
            self.match(ScriptEstagioParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotificacaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CADEIA(self, i:int=None):
            if i is None:
                return self.getTokens(ScriptEstagioParser.CADEIA)
            else:
                return self.getToken(ScriptEstagioParser.CADEIA, i)

        def AS(self):
            return self.getToken(ScriptEstagioParser.AS, 0)

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(ScriptEstagioParser.NUMERO)
            else:
                return self.getToken(ScriptEstagioParser.NUMERO, i)

        def getRuleIndex(self):
            return ScriptEstagioParser.RULE_notificacao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotificacao" ):
                listener.enterNotificacao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotificacao" ):
                listener.exitNotificacao(self)




    def notificacao(self):

        localctx = ScriptEstagioParser.NotificacaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_notificacao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(ScriptEstagioParser.T__12)
            self.state = 79
            self.match(ScriptEstagioParser.CADEIA)
            self.state = 86
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.state = 80
                self.match(ScriptEstagioParser.T__8)
                self.state = 81
                self.match(ScriptEstagioParser.CADEIA)
                pass
            elif token in [17]:
                self.state = 82
                self.match(ScriptEstagioParser.AS)
                self.state = 83
                self.match(ScriptEstagioParser.NUMERO)
                self.state = 84
                self.match(ScriptEstagioParser.T__2)
                self.state = 85
                self.match(ScriptEstagioParser.NUMERO)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrigemDadosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORIGEM_DADOS(self):
            return self.getToken(ScriptEstagioParser.ORIGEM_DADOS, 0)

        def CADEIA(self):
            return self.getToken(ScriptEstagioParser.CADEIA, 0)

        def getRuleIndex(self):
            return ScriptEstagioParser.RULE_origemDados

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrigemDados" ):
                listener.enterOrigemDados(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrigemDados" ):
                listener.exitOrigemDados(self)




    def origemDados(self):

        localctx = ScriptEstagioParser.OrigemDadosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_origemDados)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(ScriptEstagioParser.ORIGEM_DADOS)
            self.state = 89
            self.match(ScriptEstagioParser.CADEIA)
            self.state = 90
            self.match(ScriptEstagioParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormatoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CADEIA(self):
            return self.getToken(ScriptEstagioParser.CADEIA, 0)

        def getRuleIndex(self):
            return ScriptEstagioParser.RULE_formato

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFormato" ):
                listener.enterFormato(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFormato" ):
                listener.exitFormato(self)




    def formato(self):

        localctx = ScriptEstagioParser.FormatoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_formato)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(ScriptEstagioParser.T__14)
            self.state = 93
            self.match(ScriptEstagioParser.CADEIA)
            self.state = 94
            self.match(ScriptEstagioParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataHorasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CADEIA(self):
            return self.getToken(ScriptEstagioParser.CADEIA, 0)

        def NUMERO(self):
            return self.getToken(ScriptEstagioParser.NUMERO, 0)

        def getRuleIndex(self):
            return ScriptEstagioParser.RULE_dataHoras

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataHoras" ):
                listener.enterDataHoras(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataHoras" ):
                listener.exitDataHoras(self)




    def dataHoras(self):

        localctx = ScriptEstagioParser.DataHorasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_dataHoras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(ScriptEstagioParser.CADEIA)
            self.state = 97
            self.match(ScriptEstagioParser.T__2)
            self.state = 98
            self.match(ScriptEstagioParser.NUMERO)
            self.state = 99
            self.match(ScriptEstagioParser.T__15)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





