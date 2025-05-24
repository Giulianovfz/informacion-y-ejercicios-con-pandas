import pandas

# el sep se utiliza especificar el delimitador
# de uso(separador) como por ej: ',' ';''.',etc
data_frame = pandas.read_csv(
    "Archivos csv txt xlsx y zip/supermarkets-semi-colons.txt", sep=';')

print(f'\n\n{data_frame}')

# se le incorpora el header para mostrar
# el encabezado de las columnas
data_frame1 = pandas.read_csv(
    "Archivos adicionales/supermarkets-semi-colons.txt", sep=';', header=None)

print(f'\n\n{data_frame1}')

# para automatizar //div[@class="card-title"]/a[contains(@href, "/entry/")]
# https://www.vulnhub.com/
