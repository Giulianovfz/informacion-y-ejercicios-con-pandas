import pandas as pd

marcas = [
    "Audi",
    "Mercedes",
    "BMW",
    "Toyota"
]

precio = [
    20e3,
    30e3,
    40e3,
    25e3
]


disponibilidad = [
    True,
    False,
    False,
    True
]

diccionario = {
    "marca": marcas,
    "precio": precio,
    "disponibilidad": disponibilidad
}

tabla_df = pd.DataFrame(diccionario)

print(tabla_df)
# print(list(zip(marcas, precio, disponibilidad)))
