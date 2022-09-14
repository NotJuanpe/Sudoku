import time
import persistence
from solver import Solver
from board import Board
from exceptions import*



condicion=True
soluciones=0
matriz=[]
lista_soluciones=[]

def limpiar_matriz():
    matriz.clear()
    
def consola():
    while condicion:
        try:
            eleccion=int(input("\nSeleccione una opcion:\n1)Ingresar un tablero\n2)Guardar un tablero en disco\n"
            +"3)Resolver un tablero\n4)Guardar tablero con soluciones\n5)Recuperar de disco tablero inicial"
            +"\n6)Recuperar tablero con soluciones\n7)Mostrar por pantalla las soluciones\n"
            +"8)Mostrar por pantalla mas de una solucion\nOpcion seleccionada: "))

            if eleccion>8 or eleccion<1 :
                raise NotAValidInteger
            elif eleccion==1:
                limpiar_matriz()
                ingresar_tablero()
            elif eleccion==2:
                if len(matriz)!=0:
                    nombre_de_tablero=input("\nPara guardar el tablero ingrese un nombre: ")
                    guardar_el_tablero_en_disco(nombre_de_tablero)
                else:print("\nIntroduzca una matriz antes de guardarla")
            elif eleccion==3:
                if len(matriz)!=0:
                    soluciones=int(input("\nIndique cuantas soluciones quiere obtener: "))
                    global lista_soluciones
                    lista_soluciones=resolver_tablero(matriz,soluciones)
                else: raise NoBoardFound
            elif eleccion==4:
                if len(lista_soluciones)!=0:
                    nombre_del_archivo=input("\nPara guardar el tablero ingrese un nombre: ")
                    guardar_tablero_con_soluciones(nombre_del_archivo,lista_soluciones)
                else:print("\nNo se puede guardar sin resolver primero un tablero")    
            elif eleccion==5:
                recuperar_tablero_inicial()
            elif eleccion==6:
                recuperar_tablero_con_soluciones()
            elif eleccion==7:
                imprimir_tablero_con_soluciones()
            elif eleccion==8:
                cual_solucion_ver()
        except ValueError:
            print("\nError se deben ingresar unicamente numeros")
        except NotAValidInteger:
            print("\nError solo se acepta un numeros (del 1 al 8)")
        except NotAnInteger:
            print("\nError se deben ingresar unicamente numeros")
        except NoBoardFound:
            print("\nError introducta primero un tablero antes deseleccionar esta opcion")
        except FileNotFoundError:
            print("\nError el archivo no existe o esta mal escrito")
# el usuario debe ingresar el tablero inicil
def ingresar_tablero():
    continua =True
    while continua:    
        try:
            opcion=int(input("\nSeleccione:\n1)Para ingresar una lista.\n2)Para finlizar."
            +"\nOpcion Seleccionada: "))
            if opcion==1:
                    recibir_lista()   
            elif opcion==2:
                    continua=False
                    tamaño_matriz()
                    print("\nTablero ingresado con exito")
            else:print("\nSolo se puede seleccionar la opcion 1 o 2")
        except ValueError:
            print("\nError se deben ingresar unicamente numeros Enteros")
        except NotAValidInteger:
            print("\nError solo se acepta un numeros (del 1 al 9) y 0 como vacio")
        except NotAnInteger:
            print("\nError se deben ingresar unicamente numeros Enteros")
        except InvalidBoard:
            print("\nError el tablero no es de nxn, ingrese nuevamente la matriz")
        except InvalidBoardSize:
            print("\nError el tablero no es un cuadrado perfecto")
#recibe  las listas y las guarda en la matriz para armar el tablero inicial
def recibir_lista():
    print("Recuerde que el tablero debe ser de nxn")
    print("Formato de lista: 1,0,0,0,5,0,8,0,0") 

    lista_de_str=input("\nLista: ") .split(",") 
    lista_de_enteros=[]
    """Combierto la lista de str a una lista de int"""
    for a in lista_de_str:
        lista_de_enteros.append(int(a))
    verificar_elementos_de_lsita(lista_de_enteros)
    matriz.append(lista_de_enteros)
    print()
    print_solucion(matriz)
    verificar_matriz()
 
#los elementos deben del 0 al 9
def verificar_elementos_de_lsita(lista):
    for a in  lista:
        if a>9 or a<0:
            raise NotAValidInteger

#la cantidad de elementos deben ser iguales en todas las listas
def verificar_matriz():
    largo=len(matriz[0]) #elementos de una lista
    if largo !=3 and largo!=4 and largo !=9 and largo !=16 and largo !=32:
        limpiar_matriz()
        raise InvalidBoardSize
    for a in matriz:
        if len(a)!=largo:
            limpiar_matriz()
            raise  InvalidBoard

#la cantidad de elementos de una lista deben ser las mismas que
#la cantidad de filas de la matriz (nxn)
def tamaño_matriz():
    largo_de_matriz=len(matriz) # filas de una matriz
    if largo_de_matriz==1 or largo_de_matriz==2:
        raise InvalidBoardSize
    for a in matriz:
        if len(a)!=largo_de_matriz:
            limpiar_matriz()
            raise InvalidBoard

#Resuelve el tablero con la cantidad de soluciones solicitadas
def resolver_tablero(tablero ,cantidad_de_soluciones):
    board = Board(tablero)
    solver = Solver(board, target_solutions=cantidad_de_soluciones)
    solver.solve()
    print("Soluciones encontradas: %d"%solver.n)
    for sol in solver.solutions:
        print_solucion(sol)
    return solver.solutions

def test_bench(tablero):
    """banco de prueba que permite resolver un tablero inicial. Calcula las
    primeras 10 soluciones y mide el tiempo que le llevó resolver el tablero.
    Muestra por pantalla los resultados

    Args:
        tablero: tablero inicial
    """    
    print("Tablero inicial:")
    board = Board(tablero)
    print(board)
    solver = Solver(board, target_solutions=10)
    start = time.time()
    solver.solve()
    end = time.time()
    print("Soluciones encontradas: %d"%solver.n)
    for sol in solver.solutions:
        print(sol)
        print_solucion(sol)
    print("Tiempo de procesamiento: %s\n"%str((end-start)/10))

def print_solucion(sol):
    """Muestra por pantalla una solución con el mismo formato que un Tablero"""
    string = ""
    for row in sol:
        for i in row:
            string += "{:2d}".format(i) + "|"
        string += "\n"
    print (string)

#guarda en formato json el tablero inicial
def guardar_el_tablero_en_disco(nombre):
    persistence.guardar_en_json(nombre,matriz)
#guarda en formato shelve el tablero inicial con las soluciones calculadas
def guardar_tablero_con_soluciones(nombre_del_archivo,soluciones):
    persistence.guardar_tablero_inicial_con_soluciones_shelve(nombre_del_archivo,soluciones,matriz)

def recuperar_tablero_inicial():
    nombre_del_archivo = input("Ingrese el nombre del archivo a recuperar: ")
    archivo=persistence.recuperar_json(nombre_del_archivo)

    #limpio las listas
    limpiar_matriz()
    lista_soluciones.clear()

    #cargo el archivo y lo agrego a la matriz
    global matriz
    matriz=archivo[nombre_del_archivo]
    print("\nCargado con exito")
    
def recuperar_tablero_con_soluciones():  
    nombre_del_archivo = input("Ingrese el nombre del archivo a recuperar: ")
    global matriz
    matriz=persistence.recuperar_tablero_inicial_shelve(nombre_del_archivo)
    global lista_soluciones
    lista_soluciones=persistence.recuperar_soluciones_shelve(nombre_del_archivo)
    print("\nCargado con exito")
   
def imprimir_tablero_con_soluciones():
    if len(matriz)==0:
        print("\nNo hay un tablero actualmente")
    else:
        print("Tablero: ")
        print_solucion(matriz)
        print("----------------------")

    if len(lista_soluciones)==0:
        print("\nNo hay soluciones actualmente")
    else:
        print("Soluciones: ")
        for a in lista_soluciones:
            print_solucion(a)

def cual_solucion_ver():
    if len(lista_soluciones)==0:
        print("\nNo hay soluciones actualmente")
    elif len(lista_soluciones)==1:
        print("\nLa unica Solucion encontrada es:")
        print_solucion(lista_soluciones[0])
    else:
        soluciones=len(lista_soluciones)
        eleccion=int(input("\nEl tablero tiene "+str(soluciones)+" soluciones ,elija cual quiere ver: "))
        if eleccion >0 and eleccion <=soluciones:
            print_solucion(lista_soluciones[eleccion-1])
        else:(print("\nOpcion no valida"))

if __name__ == '__main__':
    consola()
