import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.impute import SimpleImputer
import os


print  ("inicio")
df_retail = pd.read_excel('codigo/BD/OnlineRetail.xlsx')
print (df_retail.info())
headers  = df_retail.columns


for  column in headers:
    if df_retail[column].dtype  in ("int64", float) :
        print( "la columna {} tiene un promedio de =  {} " .format(column,  df_retail[column].mean()))
        print( "la columna {} tiene un mediana de =  {} " .format(column,  df_retail[column].median()))
        print( "la columna {} tiene una desviación estandar  de =  {} " .format(column,  df_retail[column].std()))
        print( "la columna {} tiene un máximo de =  {} " .format(column,  df_retail[column].max()))
        print( "la columna {} tiene un mínimo de =  {} " .format(column,  df_retail[column].min()))
        print ("-----------------------------------------------------------------------------")
