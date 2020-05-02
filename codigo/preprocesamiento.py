import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.impute import SimpleImputer
import seaborn as sns
from Funcion1D import *
from Funcion2D import *
import os
import subprocess


#Lectura del archivo de la BD
df_bd_original = pd.read_csv('BD/OnlineRetailcsv.csv', sep=',', encoding = 'unicode_escape')

#Obtenemos el análisis 1D de la BD sin preprocesar
#Analisis1D_SinPreprocesar(df_bd_original)
#os.system("PAUSE")

####################################################################
#Ahora comenzamos a preprocesar la BD
print("\n*******COMIENZA EL PREPROCESAMIENTO*******")
#detectamos la cantidad de tuplas que tengan la columna Quantity en negativo
df_quantity_negative = df_bd_original.loc[df_bd_original['Quantity'] < 0]
#detectamos la cantidad de tuplas que tengan la columna CustomerID NULL
df_null = df_bd_original.loc[df_bd_original['CustomerID'].isna()]
#df_deletenull elimina las tuplas con CustomerID = NULL y el resultado se almacena aca mismo
df_deletenull = df_bd_original.dropna(subset=['CustomerID'])
#detecta las tuplas con Quantity negativo en la bd sin nulls
df_quantity_negative_2 = df_deletenull.loc[df_deletenull['Quantity'] < 0]
#se elimina las tuplas con Quantity negativo restantes y se almacena la BD preprocesada en df_bd_nueva
df_bd_nueva = df_deletenull.drop(df_deletenull[df_deletenull['Quantity']<0].index)
#Comprobamos si existen tuplas duplicadas
df_filas_duplicadas = df_bd_nueva[df_bd_nueva.duplicated()]
#Eliminamos las tuplas duplicadas de la BD nueva, almacenandose en df_bd_nueva_final
#Ahora obtenemos la BD nueva sin filas duplicadas
df_bd_nueva_final = df_bd_nueva.drop_duplicates()
#print(df_bd_nueva.count())

print("\nFormato de muestra de registros (cant.filas , columnastotales)\n")
print("-------------------- PREPROCESAMIENTO --------------------")
print("Cantidad de tuplas totales en la BD original:", df_bd_original.shape)
print("Cantidad de tuplas con Quantity negativo:", df_quantity_negative.shape)
print("Cantidad de tuplas con CustomerId = NULL:", df_null.shape)
print("BD nueva sin las tuplas con CustomerID = null:", df_deletenull.shape)
print("Cantidad de tuplas restantes con Quantity < 0 en la BD nueva:", df_quantity_negative_2.shape)
print("Cantidad de tuplas totales de la BD nueva preprocesada:", df_bd_nueva.shape)
print("Número de filas duplicadas: ", df_filas_duplicadas.shape)
print("Total de filas de BD nueva sin filas duplicadas: ",df_bd_nueva_final.shape)
print("----------------------------------------------------------")

#Creamos un archivo con la BD preprocesada tomando las columnas importantes que se utilizaran en este proyecto
#df_temporal = df_bd_nueva_final[['Description','Quantity','InvoiceDate', 'UnitPrice', 'CustomerID']]
#df_temporal.to_csv(r'BD\OnlineRetail_Preprocesada.csv')

#Ya tenemos la BD preprocesada almacenada en df_bd_nueva_final
df_bd_nueva_final = pd.read_csv('BD/OnlineRetail_Preprocesada.csv', sep=',', encoding = 'unicode_escape')
####################################################################


#Obtenemos el análisis 1D de la BD ya preprocesada
Analisis1D_Preprocesada(df_bd_nueva_final)
os.system("PAUSE")

print("----------------------------------------------------------")
print("\nEjecutando interfaz para análisis 2D: \n")
print("***Visualizando interfaz*** ")
#Ejecutamos el interfaz del análisis 2D para visualizar los diagramas
interfaz_analisis2D = subprocess.Popen(['python', 'interfaz.py'])
#os.system ("start interfaz.py")

#Obtenemos el análisis 2D de la BD ya preprocesada
#Analisis2D_Preprocesada(df_bd_nueva_final)
os.system("PAUSE")
print("\nEjecución del programa finalizda")

#Ahora comenzar a procesar los datos para encontrar resultados
