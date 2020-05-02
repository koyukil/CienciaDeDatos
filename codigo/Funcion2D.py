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
    #Se muestra en pantalla el Histograma de Frecuencia de productos
    ###############


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
    #Se muestra en pantalla el Histograma de Frecuencia de paises
    ###############


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
    #Se muestra en pantalla el Histograma de Frecuencia de cantidad de productos
    ###############


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
    #Se muestra en pantalla el Mapa de Calor
    ###############


    ###############

def Diagrama_de_Dispersion_cantidad_dia(csv_preprocesado):
    #Scatterplot (Diagrama de dispersión) para encontrar la correlación entre dos variables
    #Debe ser algo como "a mas valor de x, mayor valor de Y..."

    #se divide InvoiceDate en fecha y hora
    df_pivot = csv_preprocesado['InvoiceDate'].str.split(expand = True)

    #se crea nuevo DF con fecha de Pivot y Quantity  del DF original
    df_final = pd.concat([df_pivot[0],csv_preprocesado['Quantity']], axis = 1)
    #se renombra columna 0 como DATE
    df_final.rename(columns = {0: 'Date'}, inplace=True)
    #se agrupa DF según fechas y se elimina el indice
    df_final=df_final.groupby(['Date']).sum()
    df_final=df_final.reset_index()
    #se imprime scatter plot
    print("Se visualiza el Diagrama de dispersión")
    fig, ax = plt.subplots(figsize=(10,6))
    ax.scatter(df_final['Date'], df_final['Quantity'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Quantity')
    plt.title("Compra de producto por día")
    plt.show();
    print ("-----------------------------------------------------------------------------")
    #Se muestra en pantalla el Diagrama de dispersión
    ###############


def Diagrama_de_Dispersion_cantidad_mes(csv_preprocesado):
    #Scatterplot (Diagrama de dispersión) para encontrar la correlación entre dos variables
    #Debe ser algo como "a mas valor de x, mayor valor de Y..."

    #se divide InvoiceDate en fecha y hora
    df_pivot = csv_preprocesado['InvoiceDate'].str.split(expand = True)
    df_pivot = df_pivot[0].str.split(pat = "/",expand = True)
    #se crea nuevo DF con fecha de Pivot y Quantity  del DF original
    df_final = pd.concat([df_pivot[0],df_pivot[2],csv_preprocesado['Quantity']], axis = 1)
    #se renombra columna 0 como DATE
    df_final.rename(columns = {0: 'Mes', 2:'Año'}, inplace=True)

    #se agrupa DF según Mes y Año y se elimina el indice

    df_final=df_final.groupby(['Mes','Año']).sum()
    df_final=df_final.reset_index()
    #se crea nueva columna Fecha, se ordena por año y mes
    df_final['Fecha'] = df_final['Mes']+ "/" + df_final['Año']
    df_final['Mes']= df_final['Mes'].astype(int)
    df_final=df_final.sort_values(['Año','Mes'],ascending=True)

    #se imprime scatter plot
    print("Se visualiza el Diagrama de dispersión")
    fig, ax = plt.subplots(figsize=(10,6))
    ax.scatter(df_final['Fecha'], df_final['Quantity'])
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Quantity')
    plt.title("Compra de producto por Mes")
    plt.show();
    print ("-----------------------------------------------------------------------------")
    #Se muestra en pantalla el Diagrama de dispersión
    ###############

    ###############

def Analisis2D_Preprocesada(csv_preprocesado):
    #Histograma_Frecuencia_Productos(csv_preprocesado)
    #Histograma_Frecuencia_Paises(csv_preprocesado)
    #Histograma_Frecuencia_Cant_Producto(csv_preprocesado)
    #Mapa_de_Calor(csv_preprocesado)
    #Diagrama_de_Dispersion_cantidad_dia(csv_preprocesado)
    Diagrama_de_Dispersion_cantidad_mes(csv_preprocesado)
