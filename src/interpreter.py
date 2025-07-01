import argparse
from antlr4 import InputStream, CommonTokenStream
from grammar.ScriptEstagioLexer import ScriptEstagioLexer
from grammar.ScriptEstagioParser import ScriptEstagioParser
from grammar.ScriptEstagioListener import ScriptEstagioListener

class Interpretador:
    def __init__(self, arvore):
        self.arvore = arvore

    def executar(self):
        #Este exemplo cobre alguns comandos básicos
        comandos = self.arvore.comando()
        for comando in comandos:
            if comando.agendamento():
                self.interpretar_agendamento(comando.agendamento())
            elif comando.geracaoRelatorio():
                self.interpretar_geracao_relatorio(comando.geracaoRelatorio())
            elif comando.registro():
                self.interpretar_registro(comando.registro())
            elif comando.logTrabalho():
                self.interpretar_log_trabalho(comando.logTrabalho())
            elif comando.tarefaCondicional():
                self.interpretar_tarefa_condicional(comando.tarefaCondicional())
            elif comando.notificacao():
                self.interpretar_notificacao(comando.notificacao())

    def interpretar_agendamento(self, agendamento):
        tarefa = agendamento.CADEIA().getText()
        dia = agendamento.PALAVRA().getText()
        hora = f"{agendamento.NUMERO(0).getText()}:{agendamento.NUMERO(1).getText()}"
        print(f"Agendando '{tarefa}' toda {dia} às {hora}.")

    def interpretar_geracao_relatorio(self, geracao_relatorio):
        nome = geracao_relatorio.CADEIA().getText()
        origem = geracao_relatorio.origemDados().CADEIA().getText()
        formato = geracao_relatorio.formato().CADEIA().getText()
        print(f"Gerando relatório '{nome}' com dados de {origem} no formato {formato}.")

    def interpretar_registro(self, registro):
        descricao = registro.CADEIA(0).getText()
        data = registro.CADEIA(1).getText()
        print(f"Registrando atividade '{descricao}' em {data}.")

    def interpretar_log_trabalho(self, log_trabalho):
        entradas = log_trabalho.dataHoras()
        for entrada in entradas:
            data = entrada.CADEIA().getText()
            horas = entrada.NUMERO().getText()
            print(f"Log de trabalho: {data} - {horas} horas.")

    def interpretar_tarefa_condicional(self, tarefa_condicional):
        condicao = tarefa_condicional.PALAVRA().getText()
        valor = tarefa_condicional.CADEIA().getText()
        print(f"Se {condicao} == {valor}, executar comandos...")

    def interpretar_notificacao(self, notificacao):
        mensagem = notificacao.CADEIA(0).getText()
        data = notificacao.CADEIA(1).getText()
        print(f"Notificação: '{mensagem}' programada para {data}.")

def exibir_instrucoes():
    print("------------------------------------------------------")
    print("Bem-vindo ao interpretador ScriptEstagio!")
    print("Este programa interpreta comandos para agendamento de tarefas, geração de relatórios e mais.")
    print("\nSiga a estrutura dos comandos abaixo:\n")
    
    print("1. **Comando de Agendamento**:")
    print('   Estrutura: agendar "Nome da Tarefa" toda [Dia da Semana] às [Hora]')
    print('   Exemplo: agendar "Planejamento da sprint" toda Segunda às 9:00')
    
    print("\n2. **Comando de Geração de Relatório**:")
    print('   Estrutura: gerar relatorio "Nome do Relatório" { origem_dados: "Nome do Arquivo de Dados"; formato: "Formato do Relatório"; }')
    print('   Exemplo: gerar relatorio "status_projeto" { origem_dados: "progresso.csv"; formato: "xlsx"; }')
    
    print("\n3. **Comando de Registro de Atividade**:")
    print('   Estrutura: registrar "Descrição da Atividade" em "Data"')
    print('   Exemplo: registrar "Reunião com a equipe" em "2024-11-28"')
    
    print("\n4. **Comando de Log de Trabalho**:")
    print('   Estrutura: log_trabalho { data: "Data"; horas: [Número de Horas]; }')
    print('   Exemplo: log_trabalho { data: "2024-11-28"; horas: 8; }')
    
    print("\n5. **Comando Condicional de Tarefa**:")
    print('   Estrutura: se [condição] == [valor] então executar [Comando]')
    print('   Exemplo: se tarefa_completa == "sim" então executar "Gerar relatório financeiro"')
    
    print("\n6. **Comando de Notificação**:")
    print('   Estrutura: notificar "Mensagem de Notificação" em "Data"')
    print('   Exemplo: notificar "Lembrete: Reunião de planejamento" em "2024-11-30"')
    
    print("\n------------------------------------------------------")
    print("Digite seus comandos abaixo. Quando terminar, digite 'fim' para encerrar.")

def main():
    exibir_instrucoes()
    
    comandos = []
    
    while True:
        comando = input("Comando: ").strip()
        
        if comando.lower() == "fim":
            break
        
        comandos.append(comando)
    
    print("\nComandos recebidos:")
    for cmd in comandos:
        print(f"  {cmd}")

if __name__ == "__main__":
    main()