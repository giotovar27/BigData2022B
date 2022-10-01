from fileinput import filename
from lib2to3.pgen2.pgen import DFAState
from pkgutil import get_data
import pandas as pd
import os
from pathlib import Path


def main():

    # leer archivo
    data=get_data(filename="llamadas123_julio_2022_PRUEBA1.csv")
    # extrer info
    data=data
    

columna=input("Digite la columna a tratar: ")
may_min=input("Para que el texto sea en mayuscula digite M ,para minuscula m ,solo la primera letra en mayuscula 1M")


def elimina_Duplicados(data):
    #Elimina los valores duplicados    '''
    data2=data.drop_duplicates() #elimina los duplicados
    print("estructuta final ",data2.shape)
    return data2
#elimina_Duplicados(data)


def valores_nulos(data,columna):
    # FUNCION Sobrescribir valores nulos
    nulo1=data[columna].fillna('SIN DATO') # remplaza los valores nulos por la palabra sin_dato
    return nulo1
#valores_nulos(data,[columna])    


def espacios_blancos(espacio,columna):
    # Funcion Quitar espacios en blanco por columnas
    espacio1=espacio[columna].str.lstrip(' ')
#espacios_blancos(data,columna)


def estandarizar_datos(columna,may_min):
    # FUNCION estandarizar datos, mayusculas o minusculas
    dat1=columna

    if may_min=='M':
        dat2=dat1.str.upper()
        print(dat2)
    else:
        if may_min=='m':
            dat2=dat1.str.lower()
            print(dat2)
        else:
            if may_min=='1M':
                dat2=dat1.str.capitalize()
                print(dat2)
            else:
                print("la Variable que ingreso es incorrecta")
# M = MAYUSCULA  //  m = minuscula // 1M = 1ra mayuscula
#estandarizar_datos(columna,may_min) # parametros: archivo, columna, y si es mayuscula o minuscula



def caracteres_especiales(data,columna):
# Funcion Eliminar caracteres especiales
    del_caracter=data[columna].str.replace(r'''["*!ˆ/()¿¡€@<?&%#>°\:]''','', regex=True)
    print(del_caracter)
#caracteres_especiales(columna)