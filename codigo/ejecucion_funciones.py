#import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np
from sklearn.impute import SimpleImputer
#import seaborn as sns
from Funcion1D import *
from Funcion2D import *
import os

#Ya tenemos la BD preprocesada almacenada en df_bd_nueva_final
df_bd_nueva_final = pd.read_csv('BD/OnlineRetail_Preprocesada.csv', sep=',', encoding = 'unicode_escape')
#os.system("PAUSE")
####################################################################

#Obtenemos el análisis 1D de la BD ya preprocesada
#Analisis1D_Preprocesada(df_bd_nueva_final)
os.system("PAUSE")

Analisis2D_Preprocesada(df_bd_nueva_final)
os.system("PAUSE")

#print("\n-- Ahora comenzar a procesar los datos para encontrar resultados --")
