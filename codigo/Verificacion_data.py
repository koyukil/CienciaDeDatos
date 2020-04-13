import numpy as np

#detecta que columna del archivo le faltan datos
def DetectarColumna(_csv, _Arch):
    i=0 #para moverse en las columnas
    name = _csv.columns.values #se obiene nombre de las columnas
    while i in range(len(name)):
        if  _csv.isnull().any().any() == True:
            i=i+1
            i=i-1
            _Arch.write(name[i]+" faltantes: "+str(_csv[name[i]].isnull().sum())+"\n")
            _Arch.write(name[i]+" total: "+str(_csv[name[i]].count())+"\n")
        i=i+1

#verifica si le faltan datos a la tabla
def Verificar_CSV(_csv, _Arch):
    a ="\n"
    #condicion que se usa para buscar posteriormente que columna(s) le faltan datos
    if  _csv.isnull().any().any() == True:
        _Arch.write("Falta datos \n")
        DetectarColumna(_csv, _Arch)
    else:
        _Arch.write("No faltan datos \n")
    return a

#llena con -1 datos faltantes al ser tipo numerico (este es el caso en esta db"
def Llenar(_csv):
    if  _csv.isnull().any().any() == True:
        tipos = _csv.columns.to_series().groupby(_csv.dtypes).groups
        ctext = tipos[np.dtype('object')]
        columnas = _csv.columns  # lista de todas las columnas
        cnum = list(set(columnas) - set(ctext))
        for c in cnum:
            _csv[c] = _csv[c].fillna(-1)

def Eliminar(_csv):
    return _csv.dropna(inplace=True)

