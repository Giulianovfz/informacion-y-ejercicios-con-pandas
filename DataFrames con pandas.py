""" Pandas DataFrames(Marcos de datos de pandas)

¿Qué es un marco de datos?
Un Pandas DataFrame es una estructura de datos bidimensional, como una matriz bidimensional o una tabla con filas y columnas.

Ejemplo
Cree un marco de datos Pandas simple:
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 
"""
import pandas as pd

datos = {"Calorias Diarias": [420, 380, 390], "Duración": [50, 40, 50]}
# cargar datos en un objeto DataFrame:
df = pd.DataFrame(datos) # df fue el nombre que se le entrego a la variable por dataframe pero puede ser cualquier otro
print(f'\n\tvalores de la lista ordenados en columna con un identificador personalizado:\n\n{df}\n')

""" Locate Row(Localizar Fila)
Como puede ver en el resultado anterior, el DataFrame es como una tabla con filas y columnas.
Pandas usa el atributo loc para devolver una o más filas específicas (Pandas use the loc attribute to return one or more specified row(s))

Example
Regresar fila 0:
#refer to the row index:
print(df.loc[0])
"""
#referirse al índice de la fila:
print(f'\n\tvalores de la posición 0:\n\n{df.loc[0]}\n')

"""  Nota: este ejemplo devuelve una serie Pandas.

Ejemplo
Devolver fila 0 y 1:
#use a list of indexes:
print(df.loc[[0, 1]])
"""
#usar una lista de índices:
print(f'\n\tvalores de la posición 0 y 1:\n\n{df.loc[[0, 1]]}\n') # Con esta forma df.loc[[0, 1]] obtenemos la primera y segunda fila

#usar una lista de índices para obtener la primera fila y mantener el formato:
print(f'\n\tvalores de la posición 0:\n\n{df.loc[[0, ]]}\n') # Con esta forma df.loc[[0, ]] obtenemos solo la primera para que se mantenga el formato

""" Nota: cuando se usa [], el resultado es un DataFrame de Pandas.

Named Indexes (Índices con nombre)

Con el argumento index, puede nombrar sus propios índices.

Ejemplo
Agrega una lista de nombres para darle un nombre a cada fila:
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

print(df) 
"""
df= pd.DataFrame(datos, index=["Día 1", "Día 2", "Día 3"])# Con esto le vamos a cambiar el indice a la tabla ahora ya no parte en 0 si no que en Día 1
print(f'\n\tvalores de la tabla:\n\n{df}\n') # Con esta forma df obtenemos toda la tabla

""" Locate Named Indexes(Localizar índices con nombre)

Utilice el índice con nombre en el atributo loc para devolver las filas especificadas. (Use the named index in the loc attribute to return the specified row(s).)

Ejemplo
Devolver "día2":

#refer to the named index:
print(df.loc["day2"])
"""
#referirse al índice nombrado:
print(f'\n\tvalores de la posición 2:\n\n{df.loc["Día 2"]}\n') # Con esta forma df.loc["Día 2"] obtenemos sólo los valores del Día 2

""" Load Files Into a DataFrame(Cargar archivos en un marco de datos)

Si sus conjuntos de datos están almacenados en un archivo, Pandas puede cargarlos en un DataFrame.

Ejemplo
Cargue un archivo separado por comas (archivo CSV) en un DataFrame:
import pandas as pd

df = pd.read_csv('data.csv')

print(df)
"""
from tkinter import filedialog
#Con esta función vamos a buscar el archivo que necesitamos en .csv
buscar_archivo = filedialog.askopenfilename(title='Buscando Archivo',filetypes=(('Tipo de archivo','*.csv'),('Todos los Archivos','*.*')))
print(buscar_archivo)

df = pd.read_csv(buscar_archivo)# Va a leer un archivo separado por comas solamente
print(f'\n\tvalores de la tabla:\n\n{df}\n')

#Aprenderá más sobre la importación de archivos en los próximos capítulos.