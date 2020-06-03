import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.impute import SimpleImputer
from scipy import stats

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
    df_pivot = df_pivot.groupby([0]).count()
    df_pivot=df_pivot.reset_index()
    valorMin = df_pivot[1].min().item() #-- Se define valor minimo de transacciones
    min = 0
    for i in range(0, len(df_pivot)): #--- Se realiza comparación para saber hora de minimás transacciones
        if valorMin == df_pivot.iloc[i][1]:
            min = df_pivot.iloc[i][0]
    print("la hora donde menos se compra es {} horas" .format(min))
