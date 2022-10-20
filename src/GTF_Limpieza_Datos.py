# -*- coding: utf-8 -*-
"""
@author: Giovanni Tovar
"""

import numpy as np
import pandas as pd
import os
from pathlib import Path
from dateutil.parser import parse
from fileinput import filename

root_dir = Path(".").resolve().parent
#print("root_dir:", root_dir)

# RUTA ARCHIVOS
data_dir = "notebooks"
path2 = os.path.join(root_dir,data_dir)
os.listdir(path2)

filename="llamadas123_julio_2022.csv"
file_path = os.path.join(root_dir,data_dir,filename)
print(file_path)

data = pd.read_csv(file_path, encoding="latin-1", sep=";")

print("estructura inicial ",data.shape)


# FUNCION Eliminar duplicados
def elimina_Duplicados(data):

    data=data.drop_duplicates() #elimina los duplicados
    return data

elimina_Duplicados(data)
n_data=elimina_Duplicados(data)
print("estructura final luego de eliminar duplicados ",n_data.shape)


# FUNCION Sobrescribir valores nulos
def valores_nulos(data):
    
    data=data.fillna('SIN DATO') # remplaza los valores nulos por la palabra sin_dato
    return data

valores_nulos(n_data)
n_data=valores_nulos(n_data)


# Funcion Quitar espacios en blanco por columnas
def espacios_blancos(data):
    
    data.iloc[:,9]=data.iloc[:,9].str.lstrip(' ')  
    data.iloc[:,8]=data.iloc[:,8].str.lstrip(' ')
    data.iloc[:,7]=data.iloc[:,7].str.lstrip(' ')
    data.iloc[:,6]=data.iloc[:,6].str.lstrip(' ')
    data.iloc[:,5]=data.iloc[:,5].str.lstrip(' ')
    data.iloc[:,3]=data.iloc[:,3].str.lstrip(' ')
    #n_data.iloc[:,[5,6,7,8,9]]=n_data.iloc[:,[5,6,7,8,9]].str.strip(' ')
    return(data)
    
espacios_blancos(n_data)
n_data=espacios_blancos(n_data)


#Funcion remplazar
def remplazo(data):
    #data=data.replace( r'''[¤]''','ñ', regex=True)
    
    replace_values={ 'Usaqu\x82n' : 'Usaquen', 'San crist¢bal': 'San Cristobal',
                    'Engativ\xa0':'Engativa', 'Los m\xa0rtires':'Los Martires',
                    'Fontib¢n':'Fontibon' }

    data=data.replace( r'''[¤]''','ñ', regex=True)
    data=data.replace( {"LOCALIDAD": replace_values} )
    return(data)

remplazo(n_data)
n_data=remplazo(n_data)

def remplazo1(data):
    data=data.replace( r'''[¡]''','i', regex=True)
    
    return(data)

remplazo1(n_data)
n_data=remplazo1(n_data)


# FUNCION estandarizar datos, primera letra Mayuscula
def estandarizar_datos(data1):
    
    #data1["RED"]=data1["RED","PRIORIDAD"].str.upper()  # MAYUSCULA
    #data1["RED"]=data1["RED"].str.lower()  # minuscula
    data1.iloc[:,9]=data1.iloc[:,9].str.capitalize()  # 1ra mayuscula
    data1.iloc[:,8]=data1.iloc[:,8].str.capitalize()
    data1.iloc[:,7]=data1.iloc[:,7].str.capitalize()
    data1.iloc[:,6]=data1.iloc[:,6].str.capitalize()
    data1.iloc[:,5]=data1.iloc[:,5].str.capitalize()
    data1.iloc[:,3]=data1.iloc[:,3].str.capitalize()
    return(data1)
    
n_data=estandarizar_datos(n_data) 

nueva_data=n_data
print(nueva_data)
