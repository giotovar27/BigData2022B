# -*- coding: utf-8 -*-
"""
@author: Giovanni Tovar
"""
from pkgutil import get_data

from tabnanny import verbose
import argparse as ap



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

def main():
    
    parser=ap.ArgumentParser()
    parser.add_argument("--verbose",type=int, default=1, help="Para imprimir informacion en pantalla")

    args=parser.parse_args()    
    #print("estructura inicial ",data.shape)


    # funcion cambio de tipo de dato
    # cambiar tipo de dato al campo edad ya que no todos los archivo vienen en el mismo tipo
def tipo_dato(data):
    
    data["EDAD"]=data["EDAD"].astype('object')
    return(data)

#data=tipo_dato(data)


# FUNCION Eliminar duplicados
def elimina_Duplicados(data):

    data=data.drop_duplicates() #elimina los duplicados
    return data

elimina_Duplicados(data)
n_data=elimina_Duplicados(data)
print("estructura inicial ",data.shape)
print("estructura final luego de eliminar duplicados ",n_data.shape)


# FUNCION Sobrescribir valores nulos
def valores_nulos(data):
    
    data=data.fillna('Sin dato') # remplaza los valores nulos por la palabra sin_dato
    return data

valores_nulos(n_data)
n_data=valores_nulos(n_data)


#Funcion remplazar
def remplazo(data):
    #data=data.replace( r'''[¤]''','ñ', regex=True)
    
    data=data.replace( r'''[¤]''','ñ', regex=True)
    data=data.replace( r'''[¡]''','i', regex=True)
    
    return(data)

remplazo(n_data)
n_data=remplazo(n_data)



# FUNCION estandarizar datos, mayusculas o minusculas
def estandarizar_datos(data1):
    
    #data1["RED"]=data1["RED","PRIORIDAD"].str.upper()  # MAYUSCULA
    #data1["RED"]=data1["RED"].str.lower()  # minuscula
    data1.iloc[:,9]=data1.iloc[:,9].str.capitalize()  # 1ra mayuscula
    data1.iloc[:,8]=data1.iloc[:,8].str.capitalize()
    data1.iloc[:,7]=data1.iloc[:,7].str.capitalize()
    data1.iloc[:,6]=data1.iloc[:,6].str.capitalize()
    data1.iloc[:,5]=data1.iloc[:,5].str.capitalize()
    data1.iloc[:,4]=data1.iloc[:,4].str.capitalize()
    data1.iloc[:,3]=data1.iloc[:,3].str.capitalize()
    return(data1)
    
n_data=estandarizar_datos(n_data) 


def remplazo(data):
    #data=data.replace( r'''[¤]''','ñ', regex=True)
    
    replace_values={ 'Usaqu\x82n' : 'Usaquen', 'Usaqun':'Usaquen','San crist¢bal': 'San Cristobal','Engativ\xa0':'Engativa', 'Los m\xa0rtires':'Los Martires',
    'Fontib¢n':'Fontibon' }
    replace_incidente= { 'Convulsi¢n' : 'Convulsion', 'Dolor tor\xa0cico': 'Dolor torácico',
    'Patologia ginecobst\x82trica':'patologia gineco obstetrica', 'Intoxicaci¢n':'Intoxicacion',
    'Electrocuci¢n / rescate':'Electrocucion / rescate' }                                                                   

    data=data.replace( {"LOCALIDAD": replace_values} )
    data=data.replace( {"TIPO_INCIDENTE": replace_incidente} )

    return(data)

remplazo(n_data)
n_data=remplazo(n_data)

print(n_data)

if __name__ == '__main__':
    main()