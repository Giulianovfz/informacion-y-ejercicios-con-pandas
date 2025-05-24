# se puede importar la librería con import pandas
# también se puede utilizar el alias pd pero se debe cambiar en la variabla también 
import pandas as pd

diccionario_de_datos = {'Automóviles': ["BWM", "Volvo", "Ford"], 'Capacidad de pasajeros': [3, 7, 2]}

mi_variable = pd.DataFrame(diccionario_de_datos)

print(mi_variable)

# con esto se que versión de pandas tengo instalada
print(f'\n\t\t¿Qué versión de pandas tengo instalada?: es la {pd.__version__}\n')
