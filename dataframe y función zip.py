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


df = pd.DataFrame(list(zip(marcas, precio, disponibilidad)),
                  columns=["marcas", "precio", "disponibilidad"])

print(df)
# print(list(zip(marcas, precio, disponibilidad)))
