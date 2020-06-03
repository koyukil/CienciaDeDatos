from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('BD/OnlineRetail_preprocesada.csv', encoding = 'unicode_escape')

#print(df.head(5))

#### Creamos Matriz de Cliente-Producto ###
#Usaremos las columnas CustomerID, StockCode y Quantity para el análisis
customer_item_matrix = df.pivot_table(index='CustomerID',columns='StockCode',values='Quantity',aggfunc='sum')

#Transformamos los números 0 a número 1 para que no interfieran en el análisis
customer_item_matrix = customer_item_matrix.applymap(lambda x: 1 if x>0 else 0)

#Creamos matriz para comparar clientes
user_to_user_sim_matrix = pd.DataFrame(cosine_similarity(customer_item_matrix))


#Configuramos las columnas de la matriz
user_to_user_sim_matrix.columns = customer_item_matrix.index
user_to_user_sim_matrix['CustomerID'] = customer_item_matrix.index
user_to_user_sim_matrix = user_to_user_sim_matrix.set_index('CustomerID')

############### Recomendaciones: ##############

#Recomendación según items comprados de un cliente A
user_to_user_sim_matrix.loc[14735.0].sort_values(ascending = False)

#Productos comprados por el cliente A
items_bought_by_A = set(customer_item_matrix.loc[14735.0].iloc[customer_item_matrix.loc[14735.0]].index)
items_bought_by_B = set(customer_item_matrix.loc[17935.0].iloc[customer_item_matrix.loc[17935.0]].index)

items_to_recommend_User_B = items_bought_by_A - items_bought_by_B

#En caso de que hayan productos duplicados en la recomendación, se eliminan
df.loc[
    df['StockCode'].isin(items_to_recommend_User_B),
    ['StockCode','Description']
].drop_duplicates().set_index('StockCode')

# ##### Walah! We just picked a random customer ID and found some recommendation items for him based on User A

# Recomendación 2: Según productos
item_item_sim_matrix = pd.DataFrame(cosine_similarity(customer_item_matrix.T))

#Usamos las mismas columnas que la matriz Cliente-Producto
item_item_sim_matrix.columns = customer_item_matrix.T.index
item_item_sim_matrix['StockCode'] = customer_item_matrix.T.index
item_item_sim_matrix = item_item_sim_matrix.set_index('StockCode')

#print(item_item_sim_matrix.head())

#Hacemos la recomendación en base a los 10 productos más similares
#El número es el producto en base a cuál se buscan los otros productos similiares
top_10_similar_items = list(
    item_item_sim_matrix\
        .loc['71053']\
        .sort_values(ascending=False)\
        .iloc[:10]\
    .index
)

print("\nRecomendación de productos:")
print(top_10_similar_items)

#En caso de que hayan productos duplicados en la recomendación, se eliminan
df.loc[
    df['StockCode'].isin(top_10_similar_items), 
    ['StockCode', 'Description']
].drop_duplicates().set_index('StockCode').loc[top_10_similar_items]