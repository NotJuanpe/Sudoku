"""
Solver de sudoku basado en backtracking
"""
class Solver:
    """Motor de backtracking que prueba todas las combinaciones posibles
    de enteros hasta encontrar una solución al tablero inicial
    """
    def __init__(self, board, target_solutions=1, callback=None):
        """Constructor

        Args:
            board (Board): tablero inicial
            target_solutions (int, opcional): Cantidad de soluciones a buscar.
            callback (funcion, optional): función a aplicar para retroceder en
            el backtracking. Se usa cuando se buscan todas las soluciones de
            un tablero inicial.
        """
        self._board = board
        self._target_solutions = target_solutions - 1
        self._solutions = []
        self._callback = callback

    def solve(self):
        """Implementa backtracking para mas info ver
        https://es.wikipedia.org/wiki/Sudoku_backtracking
        """
        if self._target_solutions >= len(self._solutions):
            if self._board.is_full():
                self._solutions.append(self._board.copia_datos)
                if self._callback:
                    self._callback(self._board)
            else:
                pos = self._board.find_next_available()
                i, j = pos
                for value in range(1, self._board.n + 1):
                    if self._board.is_plausible(i, j, value):
                        self._board.register(i, j, value)
                        self.solve()
                        self._board.delete(i, j)

    @property
    def n(self):
        """Cantidad de soluciones encontradas

        Returns:
            int: cantidad de soluciones encontradas
        """
        return len(self._solutions)

    @property
    def solutions(self):
        """Devuelve una copia de las soluciones encontradas

        Returns:
            lista de soluciones (tableros resueltos)
        """
        return [row[:] for row in self._solutions]
