# Generated from grammar/ScriptEstagio.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ScriptEstagioParser import ScriptEstagioParser
else:
    from ScriptEstagioParser import ScriptEstagioParser

# This class defines a complete listener for a parse tree produced by ScriptEstagioParser.
class ScriptEstagioListener(ParseTreeListener):

    # Enter a parse tree produced by ScriptEstagioParser#script.
    def enterScript(self, ctx:ScriptEstagioParser.ScriptContext):
        pass

    # Exit a parse tree produced by ScriptEstagioParser#script.
    def exitScript(self, ctx:ScriptEstagioParser.ScriptContext):
        pass


    # Enter a parse tree produced by ScriptEstagioParser#comando.
    def enterComando(self, ctx:ScriptEstagioParser.ComandoContext):
        pass

    # Exit a parse tree produced by ScriptEstagioParser#comando.
    def exitComando(self, ctx:ScriptEstagioParser.ComandoContext):
        pass


    # Enter a parse tree produced by ScriptEstagioParser#agendamento.
    def enterAgendamento(self, ctx:ScriptEstagioParser.AgendamentoContext):
        pass

    # Exit a parse tree produced by ScriptEstagioParser#agendamento.
    def exitAgendamento(self, ctx:ScriptEstagioParser.AgendamentoContext):
        pass


    # Enter a parse tree produced by ScriptEstagioParser#geracaoRelatorio.
    def enterGeracaoRelatorio(self, ctx:ScriptEstagioParser.GeracaoRelatorioContext):
        pass

    # Exit a parse tree produced by ScriptEstagioParser#geracaoRelatorio.
    def exitGeracaoRelatorio(self, ctx:ScriptEstagioParser.GeracaoRelatorioContext):
        pass


    # Enter a parse tree produced by ScriptEstagioParser#registro.
    def enterRegistro(self, ctx:ScriptEstagioParser.RegistroContext):
        pass

    # Exit a parse tree produced by ScriptEstagioParser#registro.
    def exitRegistro(self, ctx:ScriptEstagioParser.RegistroContext):
        pass


    # Enter a parse tree produced by ScriptEstagioParser#logTrabalho.
    def enterLogTrabalho(self, ctx:ScriptEstagioParser.LogTrabalhoContext):
        pass

    # Exit a parse tree produced by ScriptEstagioParser#logTrabalho.
    def exitLogTrabalho(self, ctx:ScriptEstagioParser.LogTrabalhoContext):
        pass


    # Enter a parse tree produced by ScriptEstagioParser#tarefaCondicional.
    def enterTarefaCondicional(self, ctx:ScriptEstagioParser.TarefaCondicionalContext):
        pass

    # Exit a parse tree produced by ScriptEstagioParser#tarefaCondicional.
    def exitTarefaCondicional(self, ctx:ScriptEstagioParser.TarefaCondicionalContext):
        pass


    # Enter a parse tree produced by ScriptEstagioParser#notificacao.
    def enterNotificacao(self, ctx:ScriptEstagioParser.NotificacaoContext):
        pass

    # Exit a parse tree produced by ScriptEstagioParser#notificacao.
    def exitNotificacao(self, ctx:ScriptEstagioParser.NotificacaoContext):
        pass


    # Enter a parse tree produced by ScriptEstagioParser#origemDados.
    def enterOrigemDados(self, ctx:ScriptEstagioParser.OrigemDadosContext):
        pass

    # Exit a parse tree produced by ScriptEstagioParser#origemDados.
    def exitOrigemDados(self, ctx:ScriptEstagioParser.OrigemDadosContext):
        pass


    # Enter a parse tree produced by ScriptEstagioParser#formato.
    def enterFormato(self, ctx:ScriptEstagioParser.FormatoContext):
        pass

    # Exit a parse tree produced by ScriptEstagioParser#formato.
    def exitFormato(self, ctx:ScriptEstagioParser.FormatoContext):
        pass


    # Enter a parse tree produced by ScriptEstagioParser#dataHoras.
    def enterDataHoras(self, ctx:ScriptEstagioParser.DataHorasContext):
        pass

    # Exit a parse tree produced by ScriptEstagioParser#dataHoras.
    def exitDataHoras(self, ctx:ScriptEstagioParser.DataHorasContext):
        pass



del ScriptEstagioParser