# # ScriptEstagio

DSL para automação de tarefas de estágio

## Equipe:

- Arthur B
- Paulo Henrique Massa Ramalho
- Pedro Henrique Valença da Rocha
- Ronaldo Lucas de Souza Silva

## Motivação:
Estagiários frequentemente realizam tarefas repetitivas e processos padronizados,
como geração de relatórios, organização de tarefas e registro de horas trabalhadas.
Essas atividades consomem tempo que poderia ser dedicado a tarefas mais produtivas.
A ScriptEstagio é uma DSL projetada para automatizar essas tarefas, oferecendo uma
sintaxe simples e intuitiva para gerenciar relatórios, agendamentos e controle de
tarefas.

Ela permite criar tarefas e agendá-las automaticamente, gerar relatórios formatados
com base em fontes de dados e registrar logs de trabalhos diários. A linguagem tem
uma sintaxe minimalista e legível, projetada para ser usada sem necessidade de amplo
treinamento prévio.

## Descrição informal da linguagem

   A ScriptEstagio possui sintaxe simples e intuitiva, com comandos como:
```
    agendar "Descrição" em "YYYY-MM-DD" — agenda uma tarefa para a data especificada.

    gerar_relatorio "tipo" de "período" — gera um relatório do tipo desejado.

    registrar_horas de HH:MM até HH:MM — registra o período de trabalho.

    notificar "mensagem" em "YYYY-MM-DD" — envia notificação na data definida.
```
## Exemplo básico

### agenda uma reunião
agendar "Reunião com equipe" em "2025-07-05"
### registra horas de trabalho
registrar_horas de 09:00 até 17:00
## Dependências

- Java 11+ (para ANTLR)
- Python 3.8+
- ANTLR 4.11.1 (antlr-4.11.1-complete.jar incluído em lib/)
- Bibliotecas Python listadas em requirements.txt
## Instalação e geração do parser

1. Clone o repositório e entre na pasta:
```
git clone
```
2. Gere o parser e lexer com ANTLR:
```
java -jar lib/antlr-4.11.1-complete.jar -Dlanguage=Python3 -o src/grammar ScriptEstagio.g4
```
3. Instale as dependências Python:
```
pip install -r requirements.txt
```
## Como executar

Para interpretar um script `.estagio`:
``` 
python3 src/interpreter.py examples/basico.estagio 
```
Para exibir ajuda:
```
python3 src/interpreter.py --help
```

## Exemplos de programas
- `examples/basico.estagio`: tarefas simples de agendamento e relatório.
-   `examples/avancado.estagio`: uso de condicionais e notificações.
## Gramática da linguagem

A gramática completa está em `ScriptEstagio.g4`. Alguns trechos:
##

> Projeto desenvolvido como parte da disciplina de Compiladores.
