[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8331309&assignment_repo_type=AssignmentRepo)
# Sudoku
Vamos a programar una aplicación que resuelva Sudokus tradicionales, donde se debe completar una cuadrícula de 9x9 con los números enteros del 1 al 9 sin que se repita el mismo número en una misma fila, misma columna o misma región. La cuadrícula de 9x9 está subdividida en 9 regiones de 3x3.
Inicalmente cada sudoku a resolver empieza con una cierta cantidad de números iniciales ya ubicados.

[Más info en Wikipedia](https://es.wikipedia.org/wiki/Sudoku)

## Ejemplo

<center>

![Sudoku a Resolver](/images/Sudoku.png)
![Sudoku Resuleto](/images/Resuelto.png)

</center>

## Módulos
### board
Representa un Sudoku como una matriz o lista bidimensional de enteros, utilizando el 0 para indicar que la celda está vacía. Por ejemplo:
```python
[[5,3,0,0,7,0,0,0,0],
 [6,0,0,1,9,5,0,0,0],
 [0,9,8,0,0,0,0,6,0],
 [8,0,0,0,6,0,0,0,3],
 [4,0,0,8,0,3,0,0,1],
 [7,0,0,0,2,0,0,0,6],
 [0,6,0,0,0,0,2,8,0],
 [0,0,0,4,1,9,0,0,5],
 [0,0,0,0,8,0,0,7,9]]
 ```
 representa el tablero del ejemplo anterior
 La clase tablero contiene métodos para:
 - Consultar si el tablero está lleno
 - Insertar y borrar un elemento en una posición dada
 - Encontrar la próxima posición vacía
 - Chequear si es posible insertar un valor en una posición dada, de acuerdo a las reglas del juego
 - Mostrar el tablero como una cadena de caracteres

 En general los tableros pueden ser de nxn, donde n debe ser un cuadrado perfecto, es decir un número cuya raíz cuadrada es un número natural. Por ejemplo 9, 16, 25, ...
 Para simplificar en nuestro tablero siempre usaremos enteros decimales en lugar de dígitos hexadecimales para tableros de 16x16, etc.

 ### exceptions
 En este modulo se definen las excepciones para tratar con tableros mal formados. Si hace falta se pueden definir más excepciones en este módulo o agregar funcionalidad a las ya definidas.
 
 ### solver
 Este módulo es capaz de resolver un Sudoku. A veces un Sudoku puede tener más de una solución posible. Este módulo es capaz de encontrar una o varias de  las soluciones posibles.
 Para resolver un Sudoku se utiliza una técnica de programación conocida como **Backtracking (vuelta atrás)** que consiste en ir probando todas las combinaciones posibles de números que se pueden colocar en las celdas vacías, pero siguiendo un plan para minimizar las cantidad de operaciones.

[Más info sobre Backtracking](https://es.wikipedia.org/wiki/Vuelta_atr%C3%A1s)

[Más info sobre resolver Sudokus con esta técnica de programación](https://es.wikipedia.org/wiki/Sudoku_backtracking)

### main (a desarrollar)
__Actualmente tiene un ejemplo de como utilizar el solver y mostrar las soluciones. Se debe reescribir.__

Aplicación de consola que ejecuta un menú que le permite al usuario:
- Ingresar un tablero inicial por teclado
- Guardar un tablero inicial en disco (json)
- Resolver un tablero, permitiendo que el usuario ingrese la cantidad máxima de soluciones a buscar. 
- Guardar un tablero inicial y las soluciones calculadas en disco (shelve)
- Recuperar de disco un tablero inicial
- Recuperar de disco un tablero inicial y las soluciones previamente calculadas.
- Mostrar por pantalla un tablero inicial y todas las soluciones calcualdas.
- Si el tablero resuelto tiene más de una solución preguntar al usuario cual quiere ver y mostrarla por pantalla.

### persistence (a desarrollar)
Módulo que permite realizar la persistencia de los tableros y soluciones, debe manejar todas las excepciones que puedan ocurrir manipulando los archivos.
Este módulo deberá permitir persistir los datos usando **_json_** para tableros iniciales, como los ejemplos y **_shelve_** para almacenar los resultados, donde se usa el nombre del tablero como clave y se guardan tanto el tablero inicial como las soluciones encontradas.
Cada archivo **_json_** corresponde a un único tablero inicial y cada archivo **_shelve_** corresponde a un tablero inicial y sus soluciones calculadas.

### Tableros
La carpeta tableros tiene varios tableros iniciales de ejemplos algunos bien formados y otros con errores. Ver README dentro de la carpeta

## Consigna
- Reescribir **_main_**
- Desarrollar el módulo **_persistence_**
- Manejar todas las situaciones excepcionales que se puedan presentar, ya sea por un error al ingresar datos por teclado, archivos de entradas mal formados, problemas al leer y escribir archivos del disco, etc.
- Escribir al menos 10 casos de pruebas unitarias con **_pytest_** y guardarlas en la carpeta **_tests_**

