import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import cut_tree

#Datos a tener en consideración:
#R: Número de días desde la última compra
#F: Frecuencia, número de transacciones
#M: Total de ingresos de las transacciones

#Lectura de la BD preprocesada
df_bd_preprocesada = pd.read_csv('BD/OnlineRetail_Preprocesada.csv', sep=',', encoding = 'unicode_escape')

#Creamos una nueva columna llamada Ingresos
df_bd_preprocesada['Ingresos'] = df_bd_preprocesada['Quantity']*df_bd_preprocesada['UnitPrice']
rfm_m = df_bd_preprocesada.groupby('CustomerID')['Ingresos'].sum()
rfm_m = rfm_m.reset_index()

#Creamos una nueva columna llamada Frecuencia
rfm_f = df_bd_preprocesada.groupby('CustomerID')['InvoiceNo'].count()
rfm_f = rfm_f.reset_index()
rfm_f.columns = ['CustomerID', 'Frecuencia']

#Se fucionan las dos nuevas columnas y se asocian al CustomerID correspondiente
rfm = pd.merge(rfm_m, rfm_f, on='CustomerID', how='inner')

#Creamos un nuevo atributo llamado ÚltimaCompra
df_bd_preprocesada['InvoiceDate'] = pd.to_datetime(df_bd_preprocesada['InvoiceDate'])

#Conocemos la última fecha donde se realizó una transacción
max_date = max(df_bd_preprocesada['InvoiceDate'])
max_date
#Conocemos la diferencia entre la última transacción y la fecha actual
df_bd_preprocesada['Diff'] = max_date - df_bd_preprocesada['InvoiceDate']

#Calculamos la última fecha de los clientes para saber la actual
rfm_p = df_bd_preprocesada.groupby('CustomerID')['Diff'].min()
rfm_p = rfm_p.reset_index()

#Extraemos el número de días desde la última transacción
rfm_p['Diff'] = rfm_p['Diff'].dt.days

#Obtenemos los datos finales de R, F y M
rfm = pd.merge(rfm, rfm_p, on='CustomerID', how='inner')
rfm.columns = ['CustomerID', 'Ingresos', 'Frecuencia', 'ÚltimaCompra']

#print(df_bd_preprocesada.head(5))

#Reescalamos los atributos
rfm_df = rfm[['Ingresos', 'Frecuencia', 'ÚltimaCompra']]
scaler = StandardScaler()
rfm_df_scaled = scaler.fit_transform(rfm_df)
rfm_df_scaled = pd.DataFrame(rfm_df_scaled)
rfm_df_scaled.columns = ['Ingresos', 'Frecuencia', 'ÚltimaCompra']


################## COMENZAMOS EL CLUSTERING DE K-MEANS ##################
kmeans = KMeans(n_clusters=9, max_iter=50) #MODIFICAMOS LA CANTIDAD DE ITERACIONES Y NUMERO DE CLUSTERS
kmeans.fit(rfm_df_scaled)
kmeans.labels_

#Ahora encontramos el número óptimo de Clusters
ssd = []
range_n_clusters = [2, 3, 4, 5, 6, 7, 8, 9, 10]
for num_clusters in range_n_clusters:
    kmeans = KMeans(n_clusters=num_clusters, max_iter=50)
    kmeans.fit(rfm_df_scaled)
    
    ssd.append(kmeans.inertia_)

range_n_clusters = [2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Valores:")
for num_clusters in range_n_clusters:
    
    #Inicializamos k-means
    kmeans = KMeans(n_clusters=num_clusters, max_iter=50)
    kmeans.fit(rfm_df_scaled)
    
    cluster_labels = kmeans.labels_
    
    #Obtenemos valor de distancia entre los clusters (desde el centro al mas lejano)
    valor = silhouette_score(rfm_df_scaled, cluster_labels)
    print("\n")
    print("Para n_clusters={0}, el valor es {1}".format(num_clusters, valor))


#Podemos usar otros parámetros para ejecutar k-means. Disminuimos la cantidad de clusters
kmeans = KMeans(n_clusters=10, max_iter=50)
kmeans.fit(rfm_df_scaled)
kmeans.labels_
rfm['Cluster_Id'] = kmeans.labels_
#print(rfm.head(5))

#Utilizamos un BoxPlot para visualizar los Clusters_Id vs Ingresos
sns.boxplot(x='Cluster_Id', y='Ingresos', data=rfm)
plt.show()

#Utilizamos un BoxPlot para visualizar los Clusters_Id vs Frecuencia
sns.boxplot(x='Cluster_Id', y='Frecuencia', data=rfm)
plt.show()

#Utilizamos un BoxPlot para visualizar los Clusters_Id vs Número de días desde última compra
sns.boxplot(x='Cluster_Id', y='ÚltimaCompra', data=rfm)
plt.show() 
