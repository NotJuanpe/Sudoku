import json
import shelve
from solver import *
diccionario={}



def guardar_en_json(nombre,tablero):
    diccionario[nombre]=tablero
    with open(nombre+".json","w",)as archivo:
        json.dump(diccionario,archivo)

def guardar_tablero_inicial_con_soluciones_shelve(nombre_del_archivo,soluciones,tablero):
    if nombre_del_archivo!="tab":
        print(soluciones)
        d = shelve.open(nombre_del_archivo)
        d["tab"]=tablero
        d[nombre_del_archivo]=soluciones
        d.close()
    else:print("\nEl nombre seleccionado no esta permitido")

def recuperar_tablero_inicial_shelve(nombre_del_archivo):
    with shelve.open(nombre_del_archivo) as db:
        keys=db.keys()
        if nombre_del_archivo in keys:
            tablero_inicial=db["tab"]
            return tablero_inicial
        else: ("No Se encuentra el archivo")

def recuperar_soluciones_shelve(nombre_del_archivo):
    with shelve.open(nombre_del_archivo) as db:
        keys=db.keys()
        if nombre_del_archivo in keys:
            soluciones=db[nombre_del_archivo]
            return soluciones
        else: ("No Se encuentra el archivo")
def recuperar_json(nombre_del_archivo):
    with open(nombre_del_archivo+".json","r") as archivo:
       matriz_recuperada=json.load(archivo) 
       return matriz_recuperada
            

