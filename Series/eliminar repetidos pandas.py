import pandas as pd

print(pd.__version__)

lista=list(range(1,10))

serie=pd.Series(lista)

print(serie)

diccio={'a':10,'b':20,'c':30,'d':30,'e':10,'f':10}
serie=pd.Series(diccio)

print(serie)
'''
import numpy as np
fechas = pd.date_range ('hoy', periodos = 6) #Definir series de tiempo como índice
num_arr = np.random.randn (6, 4) # Pasar en una matriz aleatoria numpy
columnas = ['A', 'B', 'C', 'D'] # Use la lista como nombres de columna
df = pd.DataFrame(num_arr, index=dates,columns=columns)
print(df)
'''
print("duplicated") #igual a first
print(serie.duplicated())

print("dupli first:")# no marca primer repetido
print(serie.duplicated(keep='first'))
print("dupli  last:")# marca solo el primer repetido
print(serie.duplicated(keep='last'))

print("dupli  false:")# marca todos los repetidos
print(serie.duplicated(keep=False))

print(serie[serie.duplicated(keep=False)])#marca y muestra todos LOS VALORES repetidos


print(serie[~ serie.duplicated()]) # muestra los valores sin tomar en cuenta a los repetidos

# eliminar duplicados:
print(serie.drop_duplicates()) # por default el keep=first

# si fuese un Dataframe puedo seleccionar la columna:

#df.drop_duplicates(['columna'],keep='last')






