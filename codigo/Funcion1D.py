import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.impute import SimpleImputer
import seaborn as sns


def Funcion_1D_a_BD_Sin_Preprocesar(csv_no_preprocesado):
    #Análisis 1D a la BD sin preprocesar
    print("\n*******\t\tAnálsis 1D de BD sin preprocesar\t\t*******\n")
    headers  = csv_no_preprocesado.columns
    for  column in headers:
        if csv_no_preprocesado[column].dtype  in ("int64", float) :
            print( "la columna {} tiene un promedio de =  {} " .format(column,  csv_no_preprocesado[column].mean()))
            print( "la columna {} tiene un mediana de =  {} " .format(column,  csv_no_preprocesado[column].median()))
            print( "la columna {} tiene una desviación estandar  de =  {} " .format(column,  csv_no_preprocesado[column].std()))
            print( "la columna {} tiene un máximo de =  {} " .format(column,  csv_no_preprocesado[column].max()))
            print( "la columna {} tiene un mínimo de =  {} " .format(column,  csv_no_preprocesado[column].min()))
            print ("-----------------------------------------------------------------------------")
        if  csv_no_preprocesado[column].dtype  in ("object", "datetime64[ns]" ) :
            print( "la columna {} tiene como moda a =  {} " .format(column,  csv_no_preprocesado[column].mode()))
            print ("-----------------------------------------------------------------------------")

def Funcion_1D_a_BD_Preprocesada(csv_preprocesado):
    print("\n*******\t\tAnálsis 1D de BD preprocesada\t\t*******\n")

    headers  = csv_preprocesado.columns
    for  column in headers:
        if csv_preprocesado[column].dtype  in ("int64", float) :
            print( "la columna {} tiene un promedio de =  {} " .format(column,  csv_preprocesado[column].mean()))
            print( "la columna {} tiene un mediana de =  {} " .format(column,  csv_preprocesado[column].median()))
            print( "la columna {} tiene una desviación estandar  de =  {} " .format(column,  csv_preprocesado[column].std()))
            print( "la columna {} tiene un máximo de =  {} " .format(column,  csv_preprocesado[column].max()))
            print( "la columna {} tiene un mínimo de =  {} " .format(column,  csv_preprocesado[column].min()))
            print ("-----------------------------------------------------------------------------")
        if  csv_preprocesado[column].dtype  in ("object", "datetime64[ns]" ) :
            print( "la columna {} tiene como moda a =  {} " .format(column,  csv_preprocesado[column].mode()))
            print ("-----------------------------------------------------------------------------")

