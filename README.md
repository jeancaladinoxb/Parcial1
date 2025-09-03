#Parcial 1 – Lenguajes de Programación

Punto 1 – AFD para a* b* c*

Se diseñó una expresión regular para cadenas sobre {a, b, c} donde todas las a aparecen antes que las b y estas antes que las c.

La expresión es:

a* b* c*


Se implementó un AFD en Python que lee su configuración desde un archivo Conf1.txt y procesa cadenas que vienen de Cadenas.txt.

El programa muestra si la cadena es aceptada o rechazada, junto con el recorrido de estados.

#Punto 2 – AFD para Identificadores

Se usó la expresión regular:

[A-Za-z][A-Za-z0-9]*


El AFD también está definido en un archivo de configuración (Conf2.txt) y se adapta al mismo programa del punto 1.

Se agregó una función para clasificar cada carácter como letra, dígito u otro.

Se hicieron pruebas con identificadores válidos.

#Punto 3 – Calculadora con Flex y Bison

Se implementó una calculadora en C con operaciones básicas  valor absoluto y raíz cuadrada.

Se trabajó con números reales doublE en vez de enteros.

Se utilizó un archivo .y gramática en Bison y un archivo .l scanner en Flex.

La entrada se toma desde un archivo de texto y la salida se muestra en consola.

Se hicieron pruebas con expresiones como:

sqrt 9
3 + sqrt 16
| -5 |
2.5 * 4

#Punto 4 – Comparación Compilado vs Interpretado

Se usó la función recursiva de Fibonacci.

Se implementó en:

C (compilado) con clock() para medir el tiempo.

Python (interpretado) con time.time().

Se calcularon valores como Fib(40) y se compararon los tiempos de ejecución.

Se observó que C ejecuta mucho más rápido que Python en este caso.

#Punto 5 – ANTLR y Fibonacci

Se creó una gramática en ANTLR (punto5.g4) para reconocer expresiones del tipo:

FIBO(8)


(el literal puede cambiarse por otro, como FIBONACCI o SERIE).

Se generó el parser en Python con ANTLR4.

En el programa principal (main.py) se obtiene el número y se calcula la secuencia de Fibonacci hasta ese valor.

Ejemplo:

Entrada:  FIBO(8)
Salida:   0, 1, 1, 2, 3, 5, 8, 13

Cómo compilar y ejecutar

Punto 1 y 2:

python3 Punto1.py
python3 Punto2.py


Punto 3:

bison -d punto3.y
flex punto3.l
gcc punto3.tab.c lex.yy.c -lm -lfl -o calc
./calc input.txt


Punto 4:

gcc fib.c -o fib
./fib
python3 fib.py


Punto 5:

antlr4 -Dlanguage=Python3 punto5.g4
python3 main.py


