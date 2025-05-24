""" Pandas Series
¿Qué es una Serie?
Una Serie Pandas es como una columna en una tabla. 
Es una matriz unidimensional que contiene datos de cualquier tipo.

Ejemplo
Cree una Serie Pandas simple a partir de una lista:

import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)
"""

from cgi import print_arguments
import pandas as pd

lista = [1, 7, 2]

mi_variable = pd.Series(lista)

print(f'\n\tvalores de la lista ordenados en columna con un identificador:\n{mi_variable}\n')

""" Labels(etiquetas)
Si no se especifica nada más, los valores se etiquetan con su número de índice. El primer valor tiene el índice 0, el segundo valor tiene el índice 1, etc.
Esta etiqueta se puede utilizar para acceder a un valor especificado.

Ejemplo
Devuelve el primer valor de la Serie:

print(myvar[0])
"""
print(f'\tvalores de la posición 0: es {mi_variable[0]}\n')

""" Create Labels(Crear las etiquetas)
Con el argumento index, puede nombrar sus propias etiquetas.

Ejemplo
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)
"""
print('\n\tCreando etiquetas para la serie')
mi_variable = pd.Series(lista, index=["X", "Y", "Z"])
print(f'\n\tvalores de la lista ordenados en columna con un identificador personalizado:\n{mi_variable}\n')

""" Cuando haya creado etiquetas, puede acceder a un elemento haciendo referencia a la etiqueta.

Ejemplo
Devolver el valor de "y":
print(myvar["y"])
"""

print(f'\tvalores de la posición Y: es {mi_variable["Y"]}\n')

""" Key/Value Objects as Series (Objetos clave/valor como serie)

También puede usar un objeto clave/valor, como un diccionario, al crear una serie

Ejemplo
Crea una Serie Pandas simple a partir de un diccionario:
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)
"""

calorias_diarias = {"Día 1": 420, "Día 2": 380, "Día 3": 390}

variable_calorias = pd.Series(calorias_diarias)
print(f'\n\tvalores de la lista ordenados en columna con un identificador personalizado:\n{variable_calorias}\n')

""" Nota: Las claves del diccionario se convierten en etiquetas.

Para seleccionar solo algunos de los elementos del diccionario, use el argumento de índice y especifique solo los elementos que desea incluir en la Serie.

Ejemplo
Cree una serie usando solo datos de "day1" y "day2":
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)
"""
print('\t\tSe imprimiran en pantalla solo los valores de Día 1 y Día 2\n')
variable_calorias2 = pd.Series(calorias_diarias, index=["Día 1", "Día 2"])
print(f'\n\tvalores de la lista ordenados en columna con un identificador personalizado:\n{variable_calorias2}\n')

""" DataFrames(marcos de datos)
Los conjuntos de datos en Pandas suelen ser tablas multidimensionales, llamadas DataFrames.
La serie es como una columna, un DataFrame es la tabla completa

Ejemplo
Cree un DataFrame a partir de dos Series:

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
"""

datos = {"Calorias Diarias": [420, 380, 390], "Duración": [50, 40, 50]}

variable_de_datos = pd.DataFrame(datos)
print(f'\n\tvalores de la lista ordenados en columna con un identificador personalizado:\n\n{variable_de_datos}\n')