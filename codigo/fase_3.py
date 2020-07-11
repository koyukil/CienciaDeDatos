from fase2_funciones import *
from Apriori import *
import os
import subprocess
from time import time

df_bd_preprocesada = pd.read_csv('BD/OnlineRetail_Preprocesada.csv', sep=',', encoding = 'unicode_escape')
df_pivot = df_bd_preprocesada['InvoiceDate'].str.split(expand = True)
df_pivot.rename(columns = {0: 'Fecha', 1: 'Hora'}, inplace=True)
df_bd_preprocesada = df_bd_preprocesada.drop(columns =['Unnamed: 0','InvoiceDate'])
df_bd_preprocesada = pd.concat([df_bd_preprocesada,df_pivot], axis = 1)
df_bd_preprocesada['Monto'] = df_bd_preprocesada['UnitPrice'] * df_bd_preprocesada['Quantity']



#--------------------Llamado a funciones ------------------
"""
articulos_libras_promedio (df_bd_preprocesada)
grupo_cliente(df_bd_preprocesada)5
numero_transacciones(df_bd_preprocesada)
"""
#---------------------Apriori general, soporte 0.01, confianza, confianza 0.1
print("\n------------ Apriori general  ---------- \n")
start_time = time()
apriori_general = a_priori(df_bd_preprocesada, 0.01, 0.1)
elapsed_time = time() - start_time
print("tiempo: %0.10f segundos. \n" % elapsed_time)


print("número de reglas de asocación : {} \n".format(len(apriori_general)))

#--------------------Se ejecuta el archivo Apriori.py-------------
dfr = []
df_association_rules = []

#------------Enfoque particional, Soporte original 0.01,  confianza original 0.1 ----------
#------------se utilizarzán parcticiones de 2,4,6,8 y 10 ----------
print("\n------------ Enfoque particional  ---------- \n")

for i in range(10):
    print( " \nPartición  número : {} \n " .format(i+1))
    dfr.append(df_bd_preprocesada.sample(frac=0.1))
    start_time = time() #tiempo inicial
    df_association_rules.append(  a_priori(dfr[i], 0.001, 0.1))
    elapsed_time = time() - start_time #tiempo final
    print("tiempo: %0.10f segundos." % elapsed_time)
    print("número de reglas de asocación : {} " .format(len(df_association_rules[i])))
    print("\n----------------------------------------------- \n")
#Soporte, Confianza, respectivamente

#"------------ fin de apriori en particiones, se debe comparar con el general----------"
contador=0
for df in range(10):
    for i in apriori_general:
        for j in df_association_rules[df]:
            if i == j:
                contador  +=  1
    print("cantidad de coincidencias de partición {} con  apriori apriori general : {}" .format((df+1), contador))
    contador = 0
