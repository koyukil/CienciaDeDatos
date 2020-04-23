import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_bd_original = pd.read_csv('BD/OnlineRetailcsv.csv', sep=',', encoding = 'unicode_escape')

df_quantity_negative = df_bd_original.loc[df_bd_original['Quantity'] < 0]

df_null = df_bd_original.loc[df_bd_original['CustomerID'].isna()]

df_deletenull = df_bd_original.dropna(subset=['CustomerID'])
#df_deletenull almacena la BD resultante sin los CustomID = null

df_nuevo_sin_negativo = df_deletenull.drop(df_deletenull[df_deletenull['Quantity']<0].index)

df_quantity_negative_2 = df_deletenull.loc[df_deletenull['Quantity'] < 0]
#detecta 8mil y algo tuplas con quantity negativo (en la bd sin nulls)


print("original", df_bd_original.shape)
print("quatity negativo", df_quantity_negative.shape)
print("null", df_null.shape)
print("nuevo BD sin null", df_deletenull.shape)
print("Quantity restantos en df_deletenull", df_quantity_negative_2.shape)
print("bla bla bla", df_nuevo_sin_negativo.shape)


#ahora comenzar a procesar los datos para encontrar resultados