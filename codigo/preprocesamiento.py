import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.impute import SimpleImputer

#Lectura del archivo de la BD
df_bd_original = pd.read_csv('BD/OnlineRetailcsv.csv', sep=',', encoding = 'unicode_escape')

#Análisis 1D a la BD sin preprocesar
print("\nAnálsis 1D BD sin preprocesar:\n")
headers  = df_bd_original.columns
for  column in headers:
    if df_bd_original[column].dtype  in ("int64", float) :
        print( "la columna {} tiene un promedio de =  {} " .format(column,  df_bd_original[column].mean()))
        print( "la columna {} tiene un mediana de =  {} " .format(column,  df_bd_original[column].median()))
        print( "la columna {} tiene una desviación estandar  de =  {} " .format(column,  df_bd_original[column].std()))
        print( "la columna {} tiene un máximo de =  {} " .format(column,  df_bd_original[column].max()))
        print( "la columna {} tiene un mínimo de =  {} " .format(column,  df_bd_original[column].min()))
        print ("-----------------------------------------------------------------------------")
    if  df_bd_original[column].dtype  in ("object", "datetime64[ns]" ) :
        print( "la columna {} tiene como moda a =  {} " .format(column,  df_bd_original[column].mode()))
        print ("-----------------------------------------------------------------------------")

#Ahora comenzamos a preprocesar la BD
print("\n*******COMIENZA EL PREPROCESAMIENTO*******")
df_quantity_negative = df_bd_original.loc[df_bd_original['Quantity'] < 0]
#detectamos la cantidad de tuplas que tengan la columna Quantity en negativo
df_null = df_bd_original.loc[df_bd_original['CustomerID'].isna()]
#detectamos la cantidad de tuplas que tengan la columna CustomerID NULL
df_deletenull = df_bd_original.dropna(subset=['CustomerID'])
#df_deletenull elimina las tuplas con CustomerID = NULL y el resultado se almacena aca mismo
df_quantity_negative_2 = df_deletenull.loc[df_deletenull['Quantity'] < 0]
#detecta las tuplas con Quantity negativo en la bd sin nulls
df_bd_nueva = df_deletenull.drop(df_deletenull[df_deletenull['Quantity']<0].index)
#se elimina las tuplas con Quantity negativo restantes y se almacena la BD preprocesada en df_bd_nueva

print("\nFormato de muestra de registros (cant.filas , columnastotales)\n")
print("-------------------- PREPROCESAMIENTO --------------------")
print("Cantidad de tuplas totales en la BD original:", df_bd_original.shape)
print("Cantidad de tuplas con Quantity negativo:", df_quantity_negative.shape)
print("Cantidad de tuplas con CustomerId = NULL:", df_null.shape)
print("BD nueva sin las tuplas con CustomerID = null:", df_deletenull.shape)
print("Cantidad de tuplas restantes con Quantity < 0 en la BD nueva:", df_quantity_negative_2.shape)
print("Cantidad de tuplas totales de la BD nueva preprocesada:", df_bd_nueva.shape)
print("----------------------------------------------------------")
#Ya tenemos la BD preprocesada almacenada en df_bd_nueva

#Análsis 1D de BD preprocesada
print("\nAnálsis 1D de BD preprocesada:\n")

headers  = df_bd_nueva.columns
for  column in headers:
    if df_bd_nueva[column].dtype  in ("int64", float) :
        print( "la columna {} tiene un promedio de =  {} " .format(column,  df_bd_nueva[column].mean()))
        print( "la columna {} tiene un mediana de =  {} " .format(column,  df_bd_nueva[column].median()))
        print( "la columna {} tiene una desviación estandar  de =  {} " .format(column,  df_bd_nueva[column].std()))
        print( "la columna {} tiene un máximo de =  {} " .format(column,  df_bd_nueva[column].max()))
        print( "la columna {} tiene un mínimo de =  {} " .format(column,  df_bd_nueva[column].min()))
        print ("-----------------------------------------------------------------------------")
    if  df_bd_nueva[column].dtype  in ("object", "datetime64[ns]" ) :
        print( "la columna {} tiene como moda a =  {} " .format(column,  df_bd_nueva[column].mode()))
        print ("-----------------------------------------------------------------------------")

print("\n-- Ahora comenzar a procesar los datos para encontrar resultados --")

"""
#Creamos la matriz Customer-Item
#utilizamos tres columnas para crear la matriz. CustomerID, StoockCode y Quantity
customer_item_matrix = df_deletenull.pivot_table(index='CustomerID',columns='StockCode',values='Quantity',aggfunc='sum')

customer_item_matrix.loc[12481:].head()
customer_item_matrix.shape
print("\n\n")
df_deletenull['CustomerID'].nunique()
df_deletenull['StockCode'].nunique()
customer_item_matrix.loc[12348.0].sum()

#Utiizamos la función Lambda para transformar los valores distintos de cero a 0
customer_item_matrix = customer_item_matrix.applymap(lambda x: 1 if x>0 else 0)
customer_item_matrix.loc[12481:].head()

#Filtramos utilizando Sklearn
from sklearn.metrics.pairwise import cosine_similarity

#Filtramos según ID
user_to_user_sim_matrix = pd.DataFrame(cosine_similarity(customer_item_matrix))
user_to_user_sim_matrix.head()

#Seteamos la columna de la matriz para mostrar nombres y el ID del usuario
user_to_user_sim_matrix.columns = customer_item_matrix.index
user_to_user_sim_matrix['CustomerID'] = customer_item_matrix.index
user_to_user_sim_matrix = user_to_user_sim_matrix.set_index('CustomerID')
user_to_user_sim_matrix.head()

#Ahora, realizamos recomendaciones de productos
user_to_user_sim_matrix.loc[12350.0].sort_values(ascending = False)

#Mostramos los productos comprados por el primer Customer
items_bought_by_A = set(customer_item_matrix.loc[12350.0].iloc[customer_item_matrix.loc[12350.0]].index)
print("Items comprados por el primer cliente:")
print(items_bought_by_A)

#Mostramos los productos comprados por el siguiente cliente
print("Items comprados por el cliente siguiente:")
items_bought_by_B = set(customer_item_matrix.loc[17935.0].iloc[customer_item_matrix.loc[17935.0]].index)
print(items_bought_by_B)


items_to_recommend_User_B = items_bought_by_A - items_bought_by_B

print("Te recomiendo que compres: \n")
print(items_to_recommend_User_B)

df_deletenull.loc[
    df_bd_original['StockCode'].isin(items_to_recommend_User_B),
    ['StockCode','Description']
].drop_duplicates().set_index('StockCode')

#Usamos un CustomerID random para encontrar las recomendaciones de productos en base al primer Customer
###HASTA ACA, ES LA RECOMENDACIÓN SEGÚN LO COMPRADO POR EL PRIMER CUSTOMER

"""

"""
#Otro tipo basado en los productos
###AHORA ES LA RECOMENDACIÓN BASADO EN LOS PRODUCTOS COMPRADOS EN GENERAL
item_item_sim_matrix = pd.DataFrame(cosine_similarity(customer_item_matrix.T))

item_item_sim_matrix.columns = customer_item_matrix.T.index
item_item_sim_matrix['StockCode'] = customer_item_matrix.T.index
item_item_sim_matrix = item_item_sim_matrix.set_index('StockCode')

item_item_sim_matrix.head()

#Ahora hacemos las recomendaciones

top_10_similar_items = list(
    item_item_sim_matrix\
        .loc['23166']\
        .sort_values(ascending=False)\
        .iloc[:10]\
    .index
)

print(top_10_similar_items)

#Obtenemos el top10 de items similares
df_bd_original.loc[
    df_bd_original['StockCode'].isin(top_10_similar_items), 
    ['StockCode', 'Description']
].drop_duplicates().set_index('StockCode').loc[top_10_similar_items]

"""
