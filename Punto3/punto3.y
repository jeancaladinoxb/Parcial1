%{
#include <stdio.h>
#include <math.h>
void yyerror (char *s);
int yylex(void);
extern FILE *yyin;
%}

%union {
    double dval;
}

%token <dval> NUMBER
%token ADD SUB MUL DIV ABS SQRT
%token EOL
%type <dval> exp factor term

%%

calclist:
    /* vacío */
  | calclist exp EOL { printf("= %.4lf\n", $2); }
  ;

exp:
    factor           { $$ = $1; }
  | exp ADD factor   { $$ = $1 + $3; }
  | exp SUB factor   { $$ = $1 - $3; }
  ;

factor:
    term             { $$ = $1; }
  | factor MUL term  { $$ = $1 * $3; }
  | factor DIV term  { 
                        if ($3 == 0) {
                            yyerror("division por cero");
                            $$ = 0;
                        } else {
                            $$ = $1 / $3;
                        }
                      }
  ;

term:
    NUMBER           { $$ = $1; }
  | ABS term         { $$ = $2 >= 0 ? $2 : -$2; }
  | SQRT term        { $$ = sqrt($2); }
  ;

%%

int main (int argc, char **argv)
{
    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            perror(argv[1]);
            return 1;
        }
    }
    yyparse();
    return 0;
}

void yyerror(char *s)
{
    fprintf(stderr, "error: %s\n", s);
}
