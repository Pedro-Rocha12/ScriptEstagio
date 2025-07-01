# ScriptEstagio
DSL para automação de tarefas de estágio

Equipe: 
Arthur B
Paulo Henrique Massa Ramalho
Pedro Henrique Valença da Rocha
Ronaldo Lucas de Souza Silva

Motivação:
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

Descrição informal da linguagem

    A ScriptEstagio possui sintaxe simples e intuitiva, com comandos como:

    agendar "Descrição" em "YYYY-MM-DD" — agenda uma tarefa para a data especificada.

    gerar_relatorio "tipo" de "período" — gera um relatório do tipo desejado.

    registrar_horas de HH:MM até HH:MM — registra o período de trabalho.

    notificar "mensagem" em "YYYY-MM-DD" — envia notificação na data definida.