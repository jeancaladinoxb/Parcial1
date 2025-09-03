%{
#include "punto3.tab.h"
#include <stdlib.h>
%}

%%

"sqrt"      { return SQRT; }
"+"         { return ADD; }
"-"         { return SUB; }
"*"         { return MUL; }
"/"         { return DIV; }
"|"         { return ABS; }

[0-9]+(\.[0-9]+)?   { yylval.dval = atof(yytext); return NUMBER; }

\n          { return EOL; }
[ \t]       { /* ignorar espacios */ }
.           { printf("Caracter desconocido: %c\n", *yytext); }

%%

