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


def elimina_Duplicados(data):
    #Elimina los valores duplicados    '''
    data2=data.drop_duplicates() #elimina los duplicados
    print("estructuta final ",data2.shape)
    return data2
#elimina_Duplicados(data)
