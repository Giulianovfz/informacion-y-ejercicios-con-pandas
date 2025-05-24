import pandas as pd

tabla_df = pd.read_csv('Archivos csv txt xlsx y zip/avocado.csv')
# separador para el documento sep=
# tabla_df = pd.read_csv('Archivos csv txt xlsx y zip/avocado.csv', sep=',')
print(tabla_df)

# index_col con este definimos el indice del dataframe
#  En este caso Unnamed:0 es la columna 0
tabla_df = pd.read_csv('Archivos csv txt xlsx y zip/avocado.csv', index_col=0)

print(tabla_df)
# index_col con este definimos el indice del dataframe
#  En este caso escribiremos el nombre de la columna, pero esta debe contener
# valores unicos no repetidos para que se considere un indice valido
tabla_df = pd.read_csv(
    'Archivos csv txt xlsx y zip/avocado.csv', index_col=["Date"])

print(tabla_df)


# con head() puedo traer los primeros elementos de la tabla si dentro del
# parentesis no se coloca ningún número trae los primeros 5 elementos de la Dataframe
# por defecto y si ingresas un número, trae solo esos elementos
print(f'{tabla_df.head()}\n')
print(
    f'Dataframe muestra solo los primeros 10 elementos\n\n{tabla_df.head(10)}')
