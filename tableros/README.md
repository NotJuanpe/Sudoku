# Tableros de prueba

En esta carpeta los siguientes tableros iniciales son válidos y se pueden resolver, cada uno tiene una única solución posible, salvo el tablero00 que está vacío y por lo tanto admite múltiples soluciones:

- tablero00.json
- tablero01.json
- tablero02.json
- tablero03.json
- tablero04.json
- tablero05.json
- tablero06.json
- tablero07.json
- tablero08.json
- tablero09.json

y los siguientes tableros tienen errores:

- tablero10.json: contiene valores que no son enteros
- tablero11.json: contiene valores fuera del rango que corresponde según el tamaño del tablero
- tablero12.json: a una fila a la que le faltan datos
- tablero13.json: le faltan filas
- tablero14.json: le falta columnas
- tablero15.json: tablero de 8x8

Cuando se lee los tableros con errores se deberían levantar y manejar las siguientes excpeciones:

- tablero10.json: NotAnInteger
- tablero11.json: NotAValidInteger
- tablero12.json: InvalidBoard
- tablero13.json: InvalidBoard
- tablero14.json: InvalidBoard
- tablero15.json: InvalidBoardSize
