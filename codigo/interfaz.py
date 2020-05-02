from tkinter import *
from Funcion1D import *
from Funcion2D import *
import os

df_bd_nueva_final = pd.read_csv('BD/OnlineRetail_Preprocesada.csv', sep=',', encoding = 'unicode_escape')

root = Tk()
root.title("Representación 2d")
root.geometry('1000x1000')   #valores de ventamna
root.config(background = "white")

B_Histograma_frec_productos=Button( root, text ="Histograma \nFrecuencia \nProductos", command =lambda:Histograma_Frecuencia_Productos(df_bd_nueva_final))
B_Histograma_frec_productos.place (x = 100, y =100 , anchor  = "center")

B_Histograma_frec_paises=Button( root, text ="Histograma \nFrecuencia \nPaises", command =lambda:Histograma_Frecuencia_Paises(df_bd_nueva_final))
B_Histograma_frec_paises.place (x = 200, y =100 , anchor  = "center")

B_Histograma_frec_cantProductos=Button( root, text ="Histograma \nFrecuencia\nCantidad \nProductos", command =lambda:Histograma_Frecuencia_Cant_Producto(df_bd_nueva_final))
B_Histograma_frec_cantProductos.place (x = 300, y =100 , anchor  = "center")

B_Mapa_calor=Button( root, text ="Mapa\nCalor", command =lambda:Mapa_de_Calor(df_bd_nueva_final))
B_Mapa_calor.place (x = 100, y =300 , anchor  = "center")

B_dispersion_CantDia=Button( root, text ="Diagrama\nDispersión\nCantidad\nDía", command =lambda:Diagrama_de_Dispersion_cantidad_dia(df_bd_nueva_final))
B_dispersion_CantDia.place (x = 200, y =300 , anchor  = "center")

B_dispersion_CantMes=Button( root, text ="Diagrama\nDispersión\nCantidad\nMes", command =lambda:Diagrama_de_Dispersion_cantidad_mes(df_bd_nueva_final))
B_dispersion_CantMes.place (x = 300, y =300 , anchor  = "center")

root.mainloop()
