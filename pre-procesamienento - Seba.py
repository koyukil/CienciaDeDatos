import pandas as pd
from pandas import *
from sklearn.preprocessing import Imputer
from sklearn.impute import SimpleImputer
import os


df_retail = pandas.read_excel('codigo/BD/OnlineRetail.xlsx')
df_retail.head()


