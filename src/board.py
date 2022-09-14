"""
tablero de Sudoku
"""
import math


class Board:
    """
    Se define el tablero como una lista de listas, es decir una matriz
    de enteros, y se usa el 0 para indicar que la celda está vacía
    """
    def __init__(self, data):
        """Constructor, recibe una tablero inicial

        Args:
            data: lista de lista de enteros con el tablero inicial.
            La matriz debe ser cuadrada
        """

        self._data_inicial_= data
        self._data = data
        self._n = len(self._data[0]) #cantidad de digitos del tablero
        self._r = int(math.sqrt(self._n)) #cada subregión tiene un tamaño de rxr

    def is_full(self):
        """verifica si el sudoku está completo, es decir si no tiene un 0

        Returns:
            True: si está completo
            False: en otro caso
        """
        for row in self._data:
            for i in row:
                if i == 0:
                    return False
        return True

    def register(self, i, j, value):
        """registra un nuevo valor en una celda dada del tablero

        Args:
            i (entero): fila de la celda
            j (entero): columna de la celda
            value (entero): valor a agregar entre 1 y n
        """
        self._data[i][j] = value

    def delete(self, i, j):
        """elimina un valor de una celda dada. Es decir coloca un 0

        Args:
            i (entero): fila de la celda
            j (entero): columna de la celda
        """
        self._data[i][j] = 0

    def find_next_available(self):
        """Encuentra la primera posición libre en el tablero.
        Empieza a buscar por la celda (0, 0)

        Returns:
            (entero, entero): fila y columna de la primer celda
            libre encontrada
        """
        for i in range(self._n):
            for j in range(self._n):
                if self._data[i][j] == 0:
                    return i, j
        return False

    def is_plausible(self, i, j, value):
        """Chequea si es posible agregar un valor dado en una posición
        determinada, sin que ese valor entre en conflicto con la fila,
        columna o región en la que está la celda

        Args:
            i (entero): fila de la celda
            j (entero): columna de la celda
            value (entero): valor a chequear entre 1 y n

        Returns:
            True: si el valor no entra en conflicto con los valores que
            ya se encuentran en la misma fila, columna o región.
            False: en caso contrario
        """
        empty_cell = (self._data[i][j] == 0)
        column = [self._data[x][j] for x in range(self._n)]
        in_box = self._is_in_box(i - i % self._r, j - j % self._r, value)
        row    = self._data[i]

        return(empty_cell and value not in column and\
               value not in row and not in_box)

    def _is_in_box(self, fila, columna, value):
        """Dada una celda y un valor chequea si ese valor se encuentra
        en la región a la que pertenece la celda

        Args:
            fila (entero): fila de la celda
            columna (entero): columna de la celda
            value (entero): valor a chequear entre 1 y n

        Returns:
            True: si el valor ya se encuentra en la misma región.
            False: en caso contrario
        """
        for i in range(self._r):
            for j in range(self._r):
                if self._data[i + fila][j + columna] == value:
                    return True
        return False

    def __str__(self):
        """
        Similar a toString de Java, para poder mostrar el tablero por pantalla
        Lo presenta como una matriz cuadrada, utilizando 2 posiciones para
        cada entero y separa los digitos de cada fila con |

        Returns:
            string: cadena de caracteres que representa a un tablero
        """
        string = ""
        for row in self._data:
            for i in row:
                string += "{:2d}".format(i) + "|"
            string += "\n"
        return string

    def __repr__(self):
        string = ""
        for row in self._data:
            for i in row:
                string += str(i) + "|"
            string += "\n"
        return string
    @property
    def n(self):
        """getter para el atributo _n

        Returns:
            int: longitud de cada fila de datos
        """
        return self._n

    @property
    def copia_datos(self):
        """copia de los datos del tablero.

        Returns:
            lista de lista de enteros con la copia del tablero
        """
        return [row[:] for row in self._data]
