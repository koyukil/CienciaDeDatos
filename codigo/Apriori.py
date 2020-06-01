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
#------------------Se crea copia de df original--------------------
df_bd_agrupada = df_bd_preprocesada[['InvoiceNo' , 'Description']]
#------------------Se agrega , a la columna Description para separarlos al agruparlos
df_bd_agrupada[['Description']] = df_bd_agrupada[['Description']] + ','
#df_codigos =  df_bd_preprocesada[['StockCode', 'Description']].groupby('StockCode')
df_bd_agrupada = df_bd_agrupada.groupby('InvoiceNo').sum()


print("\nAplicando algoritmo A-priori...\n")

#Largo de la tabla anterior
len_records = len(df_bd_agrupada)

matriz = []
#-----------------DF agrupado por InvoiceNo se separa por las , y se agrega a matriz como  []------------
for  i in range(0, len_records):
    split = df_bd_agrupada.values[i][0].split(",")
    matriz.append(split)
#-----------------Se realiza algoritmo apriori y se imprimem las 20 mejores reglas --------------------------------
print( "top 20 reglas \n -----------------")
association_rules = apriori(matriz, min_support=0.01, min_confidence=0.6, min_lift=3, min_length=5)
for idx, x in enumerate(association_rules):
    if idx > 20:
       break
    print (x.items)

print("Ejecución del Algoritmo A-priori terminada.")
print("Presione una tecla para continuar...")
