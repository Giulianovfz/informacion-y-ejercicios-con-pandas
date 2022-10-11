""" Pandas Read CSV(Pandas Leer CSV)

Read CSV Files(Leer archivos CSV)

Una forma sencilla de almacenar grandes conjuntos de datos es utilizar archivos CSV (archivos separados por comas).
Los archivos CSV contienen texto sin formato y es un formato bien conocido que todos pueden leer, incluidos los pandas.
En nuestros ejemplos, usaremos un archivo CSV llamado 'data.csv'.

Ejemplo
Cargue el CSV en un DataFrame:
import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string()) 
"""
import pandas as pd
from tkinter import filedialog
#Con esta función vamos a buscar el archivo que necesitamos en .csv
buscar_archivo = filedialog.askopenfilename(title='Buscando Archivo',filetypes=(('Tipo de archivo','*.csv'),('Todos los Archivos','*.*')))
print(buscar_archivo)

df = pd.read_csv(buscar_archivo)# Va a leer un archivo separado por comas solamente
print(f'\n\tvalores de la tabla:\n\n{df.to_string()}\n')

""" Sugerencia: utilice to_string() para imprimir todo el DataFrame.

Si tiene un DataFrame grande con muchas filas, Pandas solo devolverá las primeras 5 filas y las últimas 5 filas:

Ejemplo
Imprima el DataFrame sin el método to_string():
import pandas as pd

df = pd.read_csv('data.csv')

print(df) 
"""
# si el archivo tiene muchas filas y columnas solo mostrara 5 columnas y 5 filas
df = pd.read_csv(buscar_archivo)# Va a leer un archivo separado por comas solamente
print(df)

""" max_rows(max_filas)

El número de filas devueltas se define en la configuración de opciones de Pandas.
Puede verificar las filas máximas de su sistema con la declaración pd.options.display.max_rows.

Ejemplo
Compruebe el número máximo de filas devueltas:
import pandas as pd

print(pd.options.display.max_rows)# pandas puede mostrar un máximo de 60 filas

En mi sistema, el número es 60, lo que significa que si el DataFrame contiene más de 60 filas, la instrucción print(df) devolverá solo los encabezados y las primeras y últimas 5 filas.
Puede cambiar el número máximo de filas con la misma instrucción.

Ejemplo
Aumente el número máximo de filas para mostrar todo el DataFrame:
import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')

print(df) 
"""

pd.options.display.max_rows = 99999 # con esto puedo mostrar 99999 filas de la variable df dentro del print

df = pd.read_csv(buscar_archivo)

print(df) 
