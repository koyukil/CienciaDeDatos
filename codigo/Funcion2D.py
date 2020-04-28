import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.impute import SimpleImputer
import seaborn as sns


def Histograma_Frecuencia_Productos(csv_preprocesado):
    #Histograma de productos: Frecuencia de aparición de variables en un intervalo
    print("Se visualiza el Histograma de Frecuencia de Productos")
    
    csv_preprocesado.Description.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
    plt.title("Frecuencia de productos")
    plt.ylabel('Frecuencia del producto')
    plt.xlabel('Producto')
    plt.show();
    print ("-----------------------------------------------------------------------------")
    ###############
    
    #Se muestra en pantalla el Histograma de Frecuencia de productos
    
    ###############
    
def Histograma_Frecuencia_Paises(csv_preprocesado):
    #Histograma de paises: Frecuencia de aparición de variables en un intervalo
    
    print("Se visualiza el Histograma de Frecuencia de Paises")
    
    csv_preprocesado.Country.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
    plt.title("Frecuencia de paises")
    plt.ylabel('Frecuencia del país')
    plt.xlabel('Pais')
    plt.show();
    print ("-----------------------------------------------------------------------------")
    ###############
    
    #Se muestra en pantalla el Histograma de Frecuencia de paises
    
    ###############
    
def Histograma_Frecuencia_Cant_Producto(csv_preprocesado):
    #Histograma de cantidad de productos: Frecuencia de aparición de variables en un intervalo
    
    print("Se visualiza el Histograma de Frecuencia de Cantidad de productos")
    
    csv_preprocesado.Quantity.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
    plt.title("Frecuencia de Cantidad de Productos")
    plt.ylabel('Frecuencia')
    plt.xlabel('Cantidad de productos')
    plt.show();
    print ("-----------------------------------------------------------------------------")
    ###############
    
    #Se muestra en pantalla el Histograma de Frecuencia de cantidad de productos
    
    ###############
    
def Mapa_de_Calor(csv_preprocesado):
    #Mapas de calor: Necesario para encontrar variables dependientes de otra(s)
    print("Se visualiza el Mapa de calor")
    
    plt.figure(figsize=(10,5))
    Mapa_calor= csv_preprocesado.corr()
    
    sns.heatmap(Mapa_calor,cmap="BrBG",annot=True)
    plt.show();
    #print(Mapa_calor)
    print ("-----------------------------------------------------------------------------")
     ###############
    
    #Se muestra en pantalla el Mapa de Calor 
    
    ###############
    
def Diagrama_de_Dispersion(csv_preprocesado):
    #Scatterplot (Diagrama de dispersión) para encontrar la correlación entre dos variables
    #Debe ser algo como "a mas valor de x, mayor valor de Y..."
    
    print("Se visualiza el Diagrama de dispersión")
    fig, ax = plt.subplots(figsize=(10,6))
    ax.scatter(csv_preprocesado['Description'], csv_preprocesado['UnitPrice'])
    ax.set_xlabel('Description')
    ax.set_ylabel('UnitPrice')
    plt.show();
    print ("-----------------------------------------------------------------------------")
    ###############
    
    #Se muestra en pantalla el Diagrama de dispersión
    
    ###############
    
def Funcion_2D_a_BD_Preprocesada(csv_preprocesado):
    Histograma_Frecuencia_Productos(csv_preprocesado)
    Histograma_Frecuencia_Paises(csv_preprocesado)
    Histograma_Frecuencia_Cant_Producto(csv_preprocesado)
    Mapa_de_Calor(csv_preprocesado)
    Diagrama_de_Dispersion(csv_preprocesado)