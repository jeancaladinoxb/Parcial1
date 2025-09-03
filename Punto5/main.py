import sys
from antlr4 import *
from punto5Lexer import punto5Lexer
from punto5Parser import punto5Parser

def fibonacci(n):
    secuencia = []
    a, b = 0, 1
    for _ in range(n):
        secuencia.append(a)
        a, b = b, a + b
    return secuencia

def main():

    data = input("Ingrese la expresión\n")

   
    input_stream = InputStream(data)
    lexer = punto5Lexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = punto5Parser(tokens)

    tree = parser.prog()  

  
    for token in tokens.tokens:
        if token.type == punto5Lexer.INT:
            n = int(token.text)

    resultado = fibonacci(n)
    print("Secuencia:", ", ".join(map(str, resultado)))

if __name__ == "__main__":
    main()
