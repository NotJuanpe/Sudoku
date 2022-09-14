"""
Módulo con las excepciones propias de la aplicación
"""
class NotAnInteger(Exception):
    """Excepción que se lanza cuando dentro de un tablero se encuentra un valor
    que no es un entero"""

class NotAValidInteger(Exception):
    """Excepción que se lanza cuando se encuentra un entero fuera de rango
    dentro de un tablero dado"""

class InvalidBoard(Exception):
    """Excepción que se lanza cuando dentro de un tablero hay filas o columnas
    con una cantidad distinta de elementos"""

class InvalidBoardSize(Exception):
    """Excepción que se lanza si n (donde el tablero es de nxn) no es un cuadrado
    perfecto"""

class NoBoardFound(Exception):
    """Excepcion que se lanza si no se introduce ningun tablero"""