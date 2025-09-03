grammar punto5;

prog: expr EOF ;

expr: 'FIBNACCI' '(' INT ')' ;

INT: [0-9]+ ;

WS: [ \t\r\n]+ -> skip ;
