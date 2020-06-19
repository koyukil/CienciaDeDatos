import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

# import required libraries for clustering
import sklearn
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import cut_tree

#Objetivo:
#Separar a los clientes  para que la empresa pueda dirigirse a sus clientes de manera eficiente.
#Datos a tener en consideración:
#R: Número de días desde la última compra
#F: Frecuencia, número de transacciones
#M: Total de ingresos de las transacciones

df_bd_preprocesada = pd.read_csv('BD/OnlineRetail_Preprocesada.csv', sep=',', encoding = 'unicode_escape')

#Creamos una nueva columna llamada Ingresos
df_bd_preprocesada['Ingresos'] = df_bd_preprocesada['Quantity']*df_bd_preprocesada['UnitPrice']
rfm_m = df_bd_preprocesada.groupby('CustomerID')['Ingresos'].sum()
rfm_m = rfm_m.reset_index()
#print(rfm_m.head(5))

#Creamos una nueva columna llamada Frecuencia New Attribute : Frecuencia
rfm_f = df_bd_preprocesada.groupby('CustomerID')['InvoiceNo'].count()
rfm_f = rfm_f.reset_index()
rfm_f.columns = ['CustomerID', 'Frecuencia']
#print(rfm_f.head(5))

#Se fucionan las dos nuevas columnas y se asocian al CustomerID correspondiente
rfm = pd.merge(rfm_m, rfm_f, on='CustomerID', how='inner')
#print(rfm.head(5))

#Creamos un nuevo atributo llamado ÚltimaCompra
df_bd_preprocesada['InvoiceDate'] = pd.to_datetime(df_bd_preprocesada['InvoiceDate'])

#Conocemos la última fecha donde se realizó una transacción
max_date = max(df_bd_preprocesada['InvoiceDate'])
max_date
#Conocemos la diferencia entre la última transacción y la fecha actual
df_bd_preprocesada['Diff'] = max_date - df_bd_preprocesada['InvoiceDate']
#print(df_bd_preprocesada.head(5))

#Calculamos la última fecha de los clientes para saber la actual
rfm_p = df_bd_preprocesada.groupby('CustomerID')['Diff'].min()
rfm_p = rfm_p.reset_index()
#rfm_p.head()

#Extraemos el número de días desde la última transacción
rfm_p['Diff'] = rfm_p['Diff'].dt.days
#rfm_p.head()

#Obtenemos los datos finales de R, F y M
rfm = pd.merge(rfm, rfm_p, on='CustomerID', how='inner')
rfm.columns = ['CustomerID', 'Ingresos', 'Frecuencia', 'ÚltimaCompra']
print(rfm.head(5))

######GRAFICO######
attributes = ['Ingresos','Frecuencia','ÚltimaCompra']
plt.rcParams['figure.figsize'] = [10,8]
sns.boxplot(data = rfm[attributes], orient="v", palette="Set2" ,whis=1.5,saturation=1, width=0.7)
plt.title("Distribución variable de valores atípicos", fontsize = 14, fontweight = 'bold')
plt.ylabel("Range", fontweight = 'bold')
plt.xlabel("Attributes", fontweight = 'bold')
print("\n Visualizamos gráfico")
plt.show()

#Reescalamos los atributos
rfm_df = rfm[['Ingresos', 'Frecuencia', 'ÚltimaCompra']]

# Instantiate
scaler = StandardScaler()
# fit_transform
rfm_df_scaled = scaler.fit_transform(rfm_df)

rfm_df_scaled = pd.DataFrame(rfm_df_scaled)
rfm_df_scaled.columns = ['Ingresos', 'Frecuencia', 'ÚltimaCompra']
#print(rfm_df_scaled.head(5))

################## COMENZAMOS EL CLUSTERING DE K-MEANS ##################
kmeans = KMeans(n_clusters=4, max_iter=50) #mODIFICAMOS LA CANTIDAD DE ITERACIONES Y NUMERO DE CLUSTERS
kmeans.fit(rfm_df_scaled)
kmeans.labels_

#Ahora encontramos el número óptimo de Clusters
ssd = []
range_n_clusters = [2, 3, 4, 5, 6, 7, 8]
for num_clusters in range_n_clusters:
    kmeans = KMeans(n_clusters=num_clusters, max_iter=50)
    kmeans.fit(rfm_df_scaled)
    
    ssd.append(kmeans.inertia_)
plt.plot(ssd)
plt.show()

range_n_clusters = [2, 3, 4, 5, 6, 7, 8]

for num_clusters in range_n_clusters:
    
    #Inicializamos k-means
    kmeans = KMeans(n_clusters=num_clusters, max_iter=50)
    kmeans.fit(rfm_df_scaled)
    
    cluster_labels = kmeans.labels_
    
    #Obtenemos valor
    valor = silhouette_score(rfm_df_scaled, cluster_labels)
    print("Valores:\n")
    print("Para n_clusters={0}, el valor es is {1}".format(num_clusters, valor))

#Podemos usar otros parámetros para ejecutar k-means. Disminuimos la cantidad de clusters
kmeans = KMeans(n_clusters=3, max_iter=50)
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

   
######### PODEMOS USAR OTRO MÉTODO, CLUSTERING JERARQUICO #########

#Enlace único
mergings = linkage(rfm_df_scaled, method="single", metric='euclidean')
dendrogram(mergings)
print("Visualizando gráfico de Enlace único")
plt.show()

#Enlace completo
mergings = linkage(rfm_df_scaled, method="complete", metric='euclidean')
dendrogram(mergings)
print("Visualizando gráfico de Enlace completo")
plt.show()

#Enlace promedio
mergings = linkage(rfm_df_scaled, method="average", metric='euclidean')
dendrogram(mergings)
print("Visualizando gráfico de Enlace promedio")
plt.show()

#Reducimos definiendo la cantidad de clusters = 3
cluster_labels = cut_tree(mergings, n_clusters=3).reshape(-1, )
cluster_labels

rfm['Cluster_Labels'] = cluster_labels
#print(rfm.head(5))

# Plot Cluster Id vs Ingresos
sns.boxplot(x='Cluster_Labels', y='Ingresos', data=rfm)
plt.show()

# Plot Cluster Id vs Frecuencia
sns.boxplot(x='Cluster_Labels', y='Frecuencia', data=rfm)
plt.show()

# Plot Cluster Id vs Número de días desde última compra
sns.boxplot(x='Cluster_Labels', y='ÚltimaCompra', data=rfm)
plt.show()

print("\nTérmino de ejecución")