# ScriptEstagio

DSL para automação de tarefas de estágio

## Equipe:

- Arthur Coimbra Bundchen
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
   
### Agendamento pontual
```agendar "Descrição da Tarefa" as 09:00;```

### Agendamento recorrente
```agendar "Reunião Semanal" toda Segunda as 10:00;```

### Geração de relatório
```
gerar relatorio "tipo_relatorio" {
  origem-dados: "dados.csv";
  formato: "json";
};
```
### Registro de horas
```
dataHoras {
  "2024-11-10": 8 horas;
  "2024-11-11": 6 horas;
};
```
### Tarefa condicional
```
se dia == "Segunda" {
  agendar "Revisar pendências" as 11:00;
};
```
### Notificação
- ```notificar "Enviar relatório semanal" em "2024-11-15";```
- ```notificar "Aviso rápido" as 17:30;```

## Exemplos básicos
- **basico.estagio**: agendamento e geração de relatório simples.
- **avancado.estagio**: blocos de `dataHoras`, uso de chaves e várias instruções.
- **controle_horas.estagio** e **tarefas_notificacoes.estagio**: demonstração de formatos alternativos de data e comandos condicionais.

## Dependências
- Java 11+ (para executar ANTLR)
- Python 3.8+
- ANTLR 4.11.1 (`antlr-4.11.1-complete.jar` em `lib/`)
- Runtime Python ANTLR: listado em `requirements.txt`

## Instalação e geração do parser

1. **Clone** este repositório:
```
git clone https://github.com/Pedro-Rocha12/ScriptEstagio.git
```
2. **Acesse** o diretório:
```
cd ScriptEstagio
```
3. **Gere** o lexer e parser Python:
```
java -jar lib/antlr-4.11.1-complete.jar -Dlanguage=Python3 -o src/grammar grammar/ScriptEstagio.g4
```
4. **Instale** o runtime Python:
```
pip install -r requirements.txt
```

## Como executar

- **Interpretar** um script `.estagio`:
```
python src/interpreter.py examples/basico.estagio
```
- **Ajuda**:
```
python src/interpreter.py --help
```

## Estrutura de diretórios
```
ScriptEstagio/
├── examples/              # Scripts de exemplo (.estagio)
├── grammar/               # Definição da gramática (ScriptEstagio.g4)
├── lib/                   # JAR do ANTLR
├── src/
│   ├── grammar/           # Artefatos gerados pelo ANTLR
│   └── interpreter.py     # Código principal do interpretador
├── requirements.txt       # Dependências Python
└── README.md              # Este arquivo
```

> *Projeto desenvolvido como parte da disciplina de Compiladores.*

