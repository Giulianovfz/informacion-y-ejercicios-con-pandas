import pandas as pd

# Método 1: Lista de listas

nombre_columnas = ["marca", "precio", "disponibilidad"]
auto_a = ["Mercedes", 10e3, True]
auto_b = ["BMW", 20e3, False]

tabla_df = pd.DataFrame([auto_a, auto_b], columns=nombre_columnas)

print(tabla_df)
