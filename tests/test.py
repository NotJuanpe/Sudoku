import os
import sys

from src.exceptions import *
from src.solver import Solver
from src.board import Board

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

def test_ingresar_matriz():
   assert 3==3

"""Traceback (most recent call last):
  File "c:\Users\Thktomahok\EstructuraDeDatos\sudoku-po\tests\test.py", line 4, in <module>
    from src.exceptions import *
ModuleNotFoundError: No module named 'src'

Intentamos realizar los test pero no logramos resolver estos errores de importacion
incluso consultamos con compañeros y aun asi no encontramos solucion"""
   

