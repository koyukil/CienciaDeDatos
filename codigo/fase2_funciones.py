import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.impute import SimpleImputer
from scipy import stats
import seaborn as sns

#-------------------------cuantos articulos en promedio se compra en cada transacción---------------------
def  articulos_libras_promedio (df_bd_preprocesada):
    df_pivot = df_bd_preprocesada[['InvoiceNo','Quantity', 'Monto']].groupby(['InvoiceNo']).sum()
    df_pivot=df_pivot.reset_index()
    media_cortada_articulos = stats.trim_mean(df_pivot['Quantity'], 0.3)
    print ( "\n-----------------------Articulos/Libras promedio-------------------------------\n ")
    print('El promedio de articulos por compra es  {} ' .format(media_cortada_articulos))
    print ( "\n------------------------------------------------------\n ")

    #print('la desviación estandar en cantidad de articulos por compra es  {} ' .format(df_pivot['Quantity'].std()))
    #print('el maximo de articulos por compra es  {} ' .format(df_pivot['Quantity'].max()))

    #-----El resultado es muy alto y poco real, eliminar valores demasiado altos para  mejorar la media-------
    #-----Solucionado con trim_mean-----------------------------------
    #---------------------Promedio de libras gastadas----------------------------
    media_cortada_monto = stats.trim_mean(df_pivot['Monto'], 0.3)
    print('El promedio de libras gastadas por compra es  {} ' .format(media_cortada_monto))
    #print('la desviación estandar de libras por compra es  {} ' .format(df_pivot['Monto'].std()))
    #print('el maximo de libras por compra es  {} ' .format(df_pivot['Monto'].max()))
    #--------------- Mismo que lo anterior----------------


#--------------------------Dividir grupo de clientes segun dinero gastado (premium/normal)-------
def grupo_cliente(df_bd_preprocesada):
    df_pivot = df_bd_preprocesada[['CustomerID', 'Monto']].groupby(['CustomerID']).sum()
    df_pivot=df_pivot.reset_index()
    MontoMedio= df_pivot[['Monto']].mean().item()
    #----------------Se define monto medio como criterio para separar clientes ----------------------
    premium= []
    normal = []
    for i in range(0, len(df_pivot)):
        if df_pivot.iloc[i]['Monto']<= MontoMedio:
            normal.append(df_pivot.iloc[i]['CustomerID'])
        else:
            premium.append(df_pivot.iloc[i]['CustomerID'])
    print ( "\n---------------------------Clasificación de clientes ---------------------------\n ")
    print("Cantidad total de clientes {}" .format(len(df_pivot)))
    print("Cantidad de clientes premium {}" .format(len(premium)))
    print("Cantidad de clientes normales {}" .format(len(normal)))


#------------------------------Intervalo de menor y mayor numero de transacciones-------------------
def numero_transacciones(df_bd_preprocesada):
    df_pivot = df_bd_preprocesada['Hora'].str.split(expand = True, pat =":")
    print ( "\n---------------------Horas de mayor/menor transacciones ---------------------------------\n ")
    print("la hora donde más se compra es {} horas" .format(df_pivot[0].mode().item()))

    df_pivot.rename(columns = {0: 'Hora'}, inplace=True)
    df_pivot.Hora.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
    plt.title("Horas de Mayor y Menor compras")
    plt.ylabel('Frecuencia del producto')
    plt.xlabel('Horario')
    plt.show()
    
#------------------------------Grafico de barras sobre compras en distintos meses-------------------    
def grafico_monto(df_bd_preprocesada):
    #Scatterplot (Diagrama de dispersión) para encontrar la correlación entre dos variables

    #se divide InvoiceDate en fecha y hora
    df_pivot = df_bd_preprocesada['Fecha'].str.split(expand = True)
    df_pivot = df_pivot[0].str.split(pat = "/",expand = True)
    #se crea nuevo DF con fecha de Pivot y Quantity del DF original
    df_final = pd.concat([df_pivot[0],df_pivot[2],df_bd_preprocesada['Monto']], axis = 1)
    #se renombra columna 0 como DATE
    df_final.rename(columns = {0: 'Mes', 2:'Año'}, inplace=True)
    df_pivot=df_final
    #se agrupa DF según Mes y Año y se elimina el indice

    df_final=df_final.groupby(['Mes','Año']).sum()
    df_final=df_final.reset_index()
    #se crea nueva columna Fecha, se ordena por año y mes
    df_final['Fecha'] = df_final['Mes']+ "/" + df_final['Año']
    df_final['Mes']= df_final['Mes'].astype(int)
    df_final=df_final.sort_values(['Año','Mes'],ascending=True)
    
    #se imprime Grafico de barras
    print("Se visualiza el Diagrama de dispersión")
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(df_final['Fecha'], df_final['Monto'])
    ax.set_xlabel('Fecha')
    ax.set_ylabel('Monto')
    plt.title("Monto por Mes")
    plt.show()
    #Se muestra en pantalla el Diagrama de dispersión
    ###############
