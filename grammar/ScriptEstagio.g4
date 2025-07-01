grammar ScriptEstagio;

//Regras léxicas
AS : 'as' | 'às' ;
A : 'à' ;
HIFEN : '-' ;
UNDERSCORE : '_' ;
ORIGEM_DADOS : 'origem-dados:' | 'origem_dados:' ;
PALAVRA : [a-zA-Z\u00C0-\u00FF]+ ;
NUMERO : [0-9]+ ;
CADEIA : '"' .*? '"' ;
ESPACO : [ \t\r\n]+ -> skip ;
COMENTARIO : '#' ~[\r\n]* -> skip ;

//Regras sintáticas
script : comando+ ;

comando
    : agendamento                //Agendamento de tarefas
    | geracaoRelatorio           //Geração de relatórios
    | registro                   //Registro de atividades
    | logTrabalho                //Horas trabalhadas
    | tarefaCondicional          //Tarefas condicionais
    | notificacao                //Envio de notificações
    ;

agendamento : 'agendar' CADEIA 'toda' PALAVRA AS NUMERO ':' NUMERO ;
geracaoRelatorio : 'gerar' 'relatorio' CADEIA '{' origemDados formato '}' ;
registro : 'registrar' CADEIA 'em' CADEIA ;
logTrabalho : 'dataHoras' '{' dataHoras+ '}' ;
tarefaCondicional : 'se' PALAVRA '==' CADEIA '{' comando+ '}' ;
notificacao : 'notificar' CADEIA ('em' CADEIA | AS NUMERO ':' NUMERO) ;

//Sub-regras para geração de relatório
origemDados : ORIGEM_DADOS CADEIA ';' ;
formato : 'formato:' CADEIA ';' ;

//Registro de horas em uma data específica
dataHoras : CADEIA ':' NUMERO 'horas;' ;