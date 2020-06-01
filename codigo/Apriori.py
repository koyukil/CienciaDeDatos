import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori
from datetime import datetime
import os
import time

df_bd_preprocesada = pd.read_csv('BD/OnlineRetail_Preprocesada.csv', sep=',', encoding = 'unicode_escape')
df_pivot = df_bd_preprocesada['InvoiceDate'].str.split(expand = True)
df_pivot.rename(columns = {0: 'Fecha', 1: 'Hora'}, inplace=True)
df_bd_preprocesada = df_bd_preprocesada.drop(columns =['Unnamed: 0','InvoiceDate'])
df_bd_preprocesada = pd.concat([df_bd_preprocesada,df_pivot], axis = 1)
df_bd_preprocesada['Monto'] = df_bd_preprocesada['UnitPrice'] * df_bd_preprocesada['Quantity']

df_codigos =  df_bd_preprocesada[['StockCode', 'Description']].groupby('StockCode')
df_bd_agrupada = df_bd_preprocesada[['InvoiceNo' , 'Description']].groupby('InvoiceNo').sum()


print("\nAplicando algoritmo A-priori...\n")

#Largo de la tabla anterior
len_records = len(df_bd_agrupada)
print(len_records)
print(df_bd_agrupada.head(5))
print(len(df_codigos))
print(df_codigos.head(5))
association_rules = apriori(df_bd_agrupada, min_support=0.2, min_confidence=0.6, min_lift=3, min_length=2)
print(association_rules)


"""
#Se genera la matriz que representa a las transacciones a utilizar y las ordena
matriz = []
# antes era 22-532-64
maxF = 5
maxL = 532
maxC  = 20
for i in range(maxF):
    a = ["nan"]*maxC
    matriz.append(a)
invoice = df_bd_ordenadas.values[0,0]
ii = 0
jj = 0
for i in range (0,maxL):
    if invoice == df_bd_ordenadas.values[i,0] and jj < maxC:
        desc = str(df_bd_ordenadas.values[i,1])
        matriz[ii][jj]=desc
        jj += 1
    else:
        ii += 1
        if ii > maxF-1:
            break
        else:
            jj = 1
            desc = str(df_bd_ordenadas.values[i,1])
            matriz[ii][0]=desc
            invoice = df_bd_ordenadas.values[i,0]
#print (matriz)

#La matriz resultante se deja en un nuevo archivo .CSV para despues usarla como parámetro
import csv
myFile = open('BD/Nueva_Matriz.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(matriz)
#print("Escritura completa")

#Se utilza el nuevo CSV generado
df_x = pd.read_csv('BD/Nueva_Matriz.csv', sep=',', encoding = 'unicode_escape', header = None)

#Se imprime el largo de columnas
#print("Cantidad de columnas de la matriz nueva:")
Cant_registros = len(df_x)
#print (Cant_registros)

Registros = []
for i in range(0, Cant_registros):
    Registros.append([str(df_x.values[i,j]) for j in range(0, maxC-1)])

#Se generan variables de tiempo para determinar cuando inicia y se termina
#tanto las reglas de asociacion como los resultados

#print("Proceso de: "+str(Cant_registros)+" x "+str(maxC)+" columnas")
#now=datetime.now()
#print ("hora de inicio (apriori): "+str(now.time()))

association_rules = apriori(Registros, min_support=0.2, min_confidence=0.6, min_lift=3, min_length=2)

#now=datetime.now()
#print ("hora de inicio (list): "+str(now.time()))

association_results = list(association_rules)

#now=datetime.now()
#print ("hora finalización: "+str(now.time()))

#Cantidad de reglas de asociación encontradas:
#print(len(association_results))

#Se imprimen las 5 primeras reglas encontradas para conocer el formato de salida y corroborar que funcione
#Se imprimiran solo 5 para este caso, ya que si se imprimieran todas el tiempo de ejecución sería muy alto
print("\nReglas de asociación:\n")
for pos in range(5):
    Reglas = association_results[pos]
    print(Reglas)
    print("\n")
    time.sleep(2)


#Se crea un ciclo for para imprimir todas las regla de asociación encontradas
#Se comenta el ciclo ya que es solo para mostrar la lógica, si se imprimieran todas tardaría mucho tiempo
for pos in range(len(association_results)):
    Reglas = association_results[pos]
    print(Reglas)
    print("\n")
    time.sleep(2)
"""
print("Ejecución del Algoritmo A-priori terminada.")
print("Presione una tecla para continuar...")
