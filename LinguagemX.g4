grammar LinguagemX;

// ------------------------------------------
// PARSER RULES (Regras de análise sintática)
// ------------------------------------------

// 1. REGRAS BÁSICAS (Expressões devem vir primeiro)
expressao
    : expressao MULT expressao     # OpMultDiv
    | expressao DIV expressao      # OpMultDiv
    | expressao SOMA expressao     # OpSomaSub
    | expressao SUB expressao      # OpSomaSub
    | expressao OP_REL expressao   # OpRelacional
    | termo                        # ExpressaoTermo
    ;

termo
    : ID                           # TermoID
    | NUM_INT                      # TermoNumInt
    | NUM_DEC                      # TermoNumDec
    | TEXTO_LITERAL                # TermoTexto
    | ABRE_PARENTESES expressao FECHA_PARENTESES # TermoParenteses
    ;

// 2. REGRAS ESTRUTURAIS
programa : (declaracao | comando)* EOF;

declaracao : (TIPO_INT | TIPO_REAL | TIPO_TEXTO) ID PONTO_VIRGULA;

comando
    : atribuicao PONTO_VIRGULA
    | io PONTO_VIRGULA
    | se_senao
    | loop_while
    | loop_for
    ;

atribuicao : ID ATRIB expressao;

io
    : LEIA ABRE_PARENTESES ID FECHA_PARENTESES
    | ESCREVA ABRE_PARENTESES expressao FECHA_PARENTESES
    ;

se_senao : IF ABRE_PARENTESES expressao FECHA_PARENTESES ABRE_CHAVE comando* FECHA_CHAVE (ELSE ABRE_CHAVE comando* FECHA_CHAVE)?;

loop_while : WHILE ABRE_PARENTESES expressao FECHA_PARENTESES ABRE_CHAVE comando* FECHA_CHAVE;

loop_for : FOR ABRE_PARENTESES atribuicao PONTO_VIRGULA expressao PONTO_VIRGULA atribuicao PONTO_VIRGULA ABRE_CHAVE comando* FECHA_CHAVE;


// ------------------------------------------
// LEXER RULES (Tokens)
// ------------------------------------------

// 1. PALAVRAS-CHAVE
TIPO_INT : 'inteiro' ;
TIPO_REAL : 'real' ;
TIPO_TEXTO : 'texto' ;

IF : 'se' ;
ELSE : 'senao' ;
WHILE : 'enquanto' ;
FOR : 'para' ;
LEIA : 'leia' ;
ESCREVA : 'escreva' ;

// 2. OPERADORES E SÍMBOLOS
ATRIB : '=' ;
SOMA : '+' ;
SUB : '-' ;
MULT : '*' ;
DIV : '/' ;
OP_REL : '==' | '!=' | '>' | '<' | '>=' | '<=' ; 

PONTO_VIRGULA : ';' ;
ABRE_PARENTESES : '(' ;
FECHA_PARENTESES : ')' ;
ABRE_CHAVE : '{' ;
FECHA_CHAVE : '}' ;

// 3. IDENTIFICADORES
ID : [a-zA-Z] ([a-zA-Z] | [0-9])* ;

// 4. LITERAIS
NUM_DEC : [0-9]+ '.' [0-9]+ ; 
NUM_INT : [0-9]+ ;
TEXTO_LITERAL : '"' ( ~["\r\n] )* '"';

// 5. IGNORAR ESPAÇOS
WS : [ \t\r\n]+ -> skip ;