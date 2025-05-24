import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#  creamos el dataframe con un archivo CSV
tabla_df = pd.read_csv("Archivos adicionales/avocado.csv")
# tabla_df = pd.read_csv("Archivos adicionales/avocado.csv", index_col=["Date"])

# mostramos los 5 primeros elementos del dataframe
print(tabla_df.head(5))


# realizamos un filtro al dataframe para buscar una región en especifico
# para este ejemplo es Chicago, por tanto creamos una variable

chicago = tabla_df[tabla_df["region"] == "Chicago"]

# también podemos cambiar el indice del dataframe después de su creación
# pero debemos guardarlo nuevamente en la varible

chicago = chicago.set_index("Date")
chicago = chicago.sort_values(by="Date")

print(chicago.head(15))

# creamos un gráfico con matplotlib

# vamos a utilizar sólo una muestra de 100 datos del dataframe
max_samples = 100

precio = chicago["AveragePrice"][:max_samples]

# creando el gráfico de los precios
plt.plot(precio, label="Precio Medio")

# Modificando el gráfico
# agregando el título del gráfico
plt.title("Precio de las Paltas vs Tiempo")

# etiqueta del eje x
plt.xlabel("Fecha")

# rotamos los textos del eje x
plt.xticks(rotation=45)

# etiqueta del eje y
plt.ylabel("Precio en $")

# mostrar lellenda de la línea
plt.legend()

# mostrando el gráfico
plt.show()
