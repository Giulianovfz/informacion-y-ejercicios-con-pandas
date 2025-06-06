# siempre pandas se importa al último para evitar errores
import numpy as np
import pandas as pd

# s = pd.Series([1, 3, 5, np.nan, 6, 8])

# print(s)
"""
Respuesta
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
"""


# Creando un DataFrame al pasar una matriz NumPy con un índice de fecha y hora usando
# date_range() y columnas etiquetadas:

dates = pd.date_range("20130101", periods=6)

print(dates)
"""
Respuesta
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
"""

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

print(df)
"""
Respuesta
                   A         B         C         D
2013-01-01  0.678643  0.248857  0.344441 -0.096724
2013-01-02 -0.353032  0.710213 -1.182660  0.674771
2013-01-03  0.159016  0.554128 -0.623259  0.391241
2013-01-04 -0.565693  1.282695  0.421631  0.550424
2013-01-05  0.248585 -2.406053  0.749259 -0.197756
2013-01-06 -1.112908  0.201061  1.177685 -0.739931
"""

# Creando un DataFrame al pasar un diccionario de objetos donde las teclas son la columna las
# Etiquetas y los valores de columna

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3]*4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)

print(f'\n{df2}')
"""
Respuesta
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
"""

# Las columnas del resultado DateFrame tienen diferentes dtypes:
print(f'\n{df2.dtypes}')
"""
Respuesta
A          float64
B    datetime64[s]
C          float32
D            int32
E         category
F           object
dtype: object
"""

# Visualizar datos

# ver el sección de funcionalidad esencialmente básica.

# Usar DataFrame.head() y DataFrame.tail() para ver la filas superior
# e inferior del marco respectivamente:

# df.head() muestra las 5 filas superiores del DataFrame
print(f'\n{df.head()}')
"""
Respuesta
                   A         B         C         D
2013-01-01  1.532572  1.586770  0.231872 -0.744719
2013-01-02  0.024336 -0.221039 -0.552782 -0.150138
2013-01-03  0.984075 -0.438600 -0.183240 -0.161141
2013-01-04  0.381048 -0.560837 -0.591970 -0.397950
2013-01-05  0.493262 -1.426376  0.499384  0.660233
"""

# df.tail() muestra las 5 filas inferiores del DataFrame
print(f'\n{df.tail(3)}')
""""
Respuesta
                   A         B         C         D
2013-01-02 -0.975320 -0.742511  1.084365 -0.690769
2013-01-03 -0.367618  0.173044 -0.513763 -1.966347
2013-01-04  0.831001 -0.460688  1.270584  0.323144
2013-01-05 -0.984666  0.900065 -1.332662 -0.594644
2013-01-06 -0.962368 -0.497102  0.473428 -0.776468
"""

# Mostrar el DataFrame.index o DataFrame.columns

# df.index
print(f'\n{df.index}')
"""
Respuesta
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')
"""

# df.columns
print(f'\n{df.columns}')
"""
Respuesta
Index(['A', 'B', 'C', 'D'], dtype='object')
"""

# Devuelva una representación Numpy de los datos subyacentes con Dataframes.to_numpy()
# sin las etiquetas de índice o columna:

print(f'\n{df.to_numpy()}')
"""
Respuesta
[[-0.52617052  0.12265608 -0.52696945 -1.04742232]
 [-0.53429252  0.59505515  0.10776525  0.1578105 ]
 [ 0.41471358 -1.72896695  0.55742226  0.95581742]
 [-1.15357745 -0.5126527  -0.02767494  0.22516405]
 [-0.66336163  0.38663305 -0.02439595 -1.56933038]
 [-0.04032016  0.17832777 -0.89044028  2.23286183]]
"""

# Nota
"""
Las matrices de NumPy tienen un dtype para toda la matriz, mientras que los pandas
DataFrames tener un dtype por columna. Cuando llamas DataFrame.to_numpy(), pandas lo
hará encuentra el dtype NumPy que puede contener todo de los dtype en el DataFrame. Si
el tipo de datos común es objet, DataFrame.to_numpy() requerirá  copiar datos.
"""

print(f'\n{df2.dtypes}')
"""
Respuesta
A          float64
B    datetime64[s]
C          float32
D            int32
E         category
F           object
dtype: object
"""

print(f'\n{df2.to_numpy()}')
"""
Respuesta
[[1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'train' 'foo']
 [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'test' 'foo']
 [1.0 Timestamp('2013-01-02 00:00:00') 1.0 3 'train' 'foo']]
"""

# describe() muestra un resumen estadístico rápido de sus datos:
print(f'\n{df2.describe()}')
"""
Respuesta
         A                    B    C    D
count  4.0                    4  4.0  4.0
mean   1.0  2013-01-02 00:00:00  1.0  3.0
min    1.0  2013-01-02 00:00:00  1.0  3.0
25%    1.0  2013-01-02 00:00:00  1.0  3.0
50%    1.0  2013-01-02 00:00:00  1.0  3.0
75%    1.0  2013-01-02 00:00:00  1.0  3.0
max    1.0  2013-01-02 00:00:00  1.0  3.0
std    0.0                  NaN  0.0  0.0
"""

# transposición de sus datos:

print(f'\n{df.T}')
"""
Respuesta
   2013-01-01  2013-01-02  2013-01-03  2013-01-04  2013-01-05  2013-01-06
A   -1.277577   -0.991470    0.919357    0.877671   -0.105184    0.545854
B    0.883263    0.935442   -0.052428   -0.329683   -0.636683   -0.597849
C    0.324609    1.308512   -0.980552    0.782017    0.279011   -1.116495
D   -0.033806   -0.707646   -0.526130   -1.522076    0.798175    0.433964
"""

# DataFrame.sort_index() ordena por un eje:

print(f'\n{df.sort_index(axis=1, ascending=False)}')
"""
Respuesta
                   D         C         B         A
2013-01-01 -0.824063 -0.907617  0.709222 -0.456044
2013-01-02 -0.427221  0.381780 -0.406825  1.921234
2013-01-03  0.079153 -0.602841  0.271903  1.705995
2013-01-04 -0.629641 -0.037520  2.379521  1.521134
2013-01-05  1.413533  1.437560 -2.088784  0.765493
2013-01-06  1.107641  0.259720  0.575463 -0.142251
"""

# DataFrame.sort_values() ordena por valores:
print(f'\n{df.sort_values(by="B")}')
"""
Respuesta
                   A         B         C         D
2013-01-02 -0.098448 -1.219873 -0.016870 -0.674318
2013-01-01  1.443728 -1.085116 -0.216788  0.256025
2013-01-05 -0.500049 -0.729936  0.130600 -1.358631
2013-01-04 -0.663113 -0.621133  0.161315 -0.593745
2013-01-06  0.663530 -0.398314 -0.885832 -1.547074
2013-01-03  1.948475 -0.285840 -1.432949  0.944602
"""

# Selección
# Nota
# Mientras que las expresiones estándar Python/NumPy para seleccionar y configurar son intuitivo
# útil para el trabajo interactivo, para el código de producción, nosotros recomendamos los métodos
# optimizados de acceso a datos de pandas, DataFrame.at(), DataFrame.iat(), DataFrame.loc() y DataFrame.iloc().


# Getitem([])
# Para un DataFrame, pasar una sola etiqueta selecciona una columna y rendimientos a Series equivalentes a df.A:
print(f'\n{df["A"]}')
"""
Respuesta
2013-01-01    0.290153
2013-01-02    0.753990
2013-01-03    0.533284
2013-01-04   -0.269497
2013-01-05   -0.375200
2013-01-06    0.896929
Freq: D, Name: A, dtype: float64
"""

# Para un DataFrame, pasando una rebanada: selecciona filas coincidentes
print(f'\n{df[0:3]}')
"""
Respuesta
                   A         B         C         D
2013-01-01  0.548821  2.328745  0.123597  0.847722
2013-01-02 -0.091691  0.104294  0.243528  0.642318
2013-01-03 -0.795440 -1.834043 -0.485659  0.167235
"""

print(f'\n{df["20130102":"20130104"]}')
"""
Respuesta
                   A         B         C         D
2013-01-02 -0.100528  0.085171 -0.684822  0.616372
2013-01-03 -0.248406 -0.480647 -2.524432 -0.287344
2013-01-04  0.596531  2.722162 -0.533863  1.574189
"""

# Selección por etiqueta
# Ver más en Selección por Etiqueta usando DataFrame.loc() o DataFrame.at()
# Seleccionar una fila que coincida con una etiqueta

print(f'\n{df.loc[dates[0]]}')
"""
Respuesta
A    0.789608
B    0.770325
C   -0.099870
D    0.842886
Name: 2013-01-01 00:00:00, dtype: float64
"""

# Selección de todas las filas : con una selección de etiquetas de columna
print(f'\n{df.loc[:, ["A", "B"]]}')
"""
Respuesta
                   A         B
2013-01-01  0.194100  0.339332
2013-01-02  1.232657  2.350722
2013-01-03 -0.362949 -2.101775
2013-01-04  1.519108 -0.667805
2013-01-05  0.118667 -0.231381
2013-01-06 -1.894757  1.102868
"""

# Para el corte de etiquetas, ambos puntos finales son incluidos:
print(f'\n{df.loc["20130102":"20130104", ["A", "B"]]}')
"""
Respuesta
                   A         B
2013-01-02  0.863857 -0.164559
2013-01-03  1.425061  1.161788
2013-01-04 -0.678148  1.985525
"""

# Seleccionar una sola fila y etiqueta de columna devuelve un escalar:
print(f'\n{df.loc[dates[0], "A"]}')
"""
Respuesta
0.6513387476738842
"""

# Para obtener acceso rápido a un escalar (equivalente al método anterior):
print(f'\n{df.at[dates[0], "A"]}')
"""
Respuesta
0.08823763553523048
"""

# Selección por posición
# Ver más en Seección por posición usando DataFrame.iloc() o DataFrame.iat()
# Seleccione a través de la posición de los enteros pasados:
print(f'\n{df.iloc[3]}')
"""
Respuesta
A   -0.263421
B   -0.178672
C   -0.072294
D   -0.634306
Name: 2013-01-04 00:00:00, dtype: float64
"""

# Los cortes enteros actuán de manera similar a NumPy/Python
print(f'{df.iloc[3:5, 0:2]}')
"""
Respuesta
                   A         B
2013-01-04  1.695126 -1.020566
2013-01-05  0.979696 -0.201327
"""

# Listas de ubicaciones de posición enteras:
print(f'\n{df.iloc[[1, 2, 4], [0, 2]]}')
"""
Respuesta
                   A         C
2013-01-02 -0.736600 -0.290705
2013-01-03  0.313971 -0.238067
2013-01-05  0.889570 -0.333174
"""

# Para cortar filas explicitamente:
print(f'\n{df.iloc[1:3, :]}')
"""
Respuesta
                   A         B         C         D
2013-01-02  1.633814  1.206762 -1.716105  0.029222
2013-01-03  0.672109  1.081313  1.286163  0.286690
"""

# Para cortar columnas explicitamente:
print(f'\n{df.iloc[:, 1:3]}')
"""
Respuesta
                   B         C
2013-01-01 -0.544621 -0.526434
2013-01-02 -0.117615 -0.193677
2013-01-03  0.987973  0.296545
2013-01-04 -1.102475  1.818261
2013-01-05  1.244797 -0.212995
2013-01-06 -1.465803  0.700264
"""

# Para obtener un valor explicitamente
print(f'\n{df.iloc[1, 1]}')
"""
Respuesta
0.056358627082930185
"""

# Para obtener acceso rápido a un escalar (equivalente al método anterior)
print(f'\n{df.iat[1, 1]}')
"""
Respuesta
0.056358627082930185
"""

# Indexación booleana
# Seleccione filas donde df.A es mayor que 0
print(f'\n{df[df["A"] > 0]}')
"""
Respuesta
2013-01-01  3.076333  0.215961 -1.141560  2.070724
2013-01-02  2.258519  0.121533  0.255179 -0.731734
2013-01-03  0.481990  0.841840 -0.041353 -0.005158
"""

# Seleccionar valores de un DataFrame donde se cumple una condición boobleana
print(f'\n{df[df > 0]}')
"""
Respuesta
                   A         B         C         D
2013-01-01  0.988819  1.125845       NaN  0.199457
2013-01-02       NaN  0.107867  1.042929  0.070091
2013-01-03  0.886842       NaN  0.071507       NaN
2013-01-04       NaN       NaN  0.224997  0.028319
2013-01-05  0.429572  1.522132       NaN       NaN
2013-01-06       NaN       NaN       NaN  0.429185
"""

# Usando isin() método para filtrar
df3 = df.copy()
df3["E"] = ["one", "one", "two", "three", "four", "three"]
print(f'\n{df3}')
"""
Respuesta
                   A         B         C         D      E
2013-01-01  0.696202  0.631313 -0.529305  0.127322    one
2013-01-02 -0.126885  0.104142 -0.697502  0.104754    one
2013-01-03  0.145180  2.459279  0.904531  1.883143    two
2013-01-04 -0.787379  1.499201 -0.410682 -0.539565  three
2013-01-05  0.488189  0.401597 -0.176248 -0.400678   four
2013-01-06  0.139619  0.204155  3.358572 -1.718699  three
"""

print(f'\n{df3[df3["E"].isin(["two", "four"])]}')
"""
Respuesta
                   A         B         C         D     E
2013-01-03 -0.228505  0.138961  0.221350 -0.457798   two
2013-01-05  1.514577  0.820687 -2.251833  0.248983  four
"""

# Configuración
# Establecer una nueva columna alinea automáticamente los datos por los índices
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130102", periods=6))

print(f'\n{s1}')
"""
Respuesta
2013-01-02    1
2013-01-03    2
2013-01-04    3
2013-01-05    4
2013-01-06    5
2013-01-07    6
Freq: D, dtype: int64
"""

df["F"] = s1

# Establecer valores por etiqueta
df.at[dates[0], "A"] = 0

# Establecer valores por posición:
df.iat[0, 1] = 0

# configuración asignando con una matriz NumPy:
df.loc[:, "D"] = np.array([5] * len(df))

print(f'\n{df}')

# Where operación con configuración
df4 = df.copy()
df4[df4 > 0] = -df4

print(f'\n{df4}')
"""
Respuesta
                   A         B         C    D    F
2013-01-01  0.000000  0.000000 -0.548565 -5.0  NaN
2013-01-02 -0.314927 -1.465733 -0.259927 -5.0 -1.0
2013-01-03 -1.864367 -0.034451 -0.395523 -5.0 -2.0
2013-01-04 -2.809433 -1.104157 -0.282051 -5.0 -3.0
2013-01-05 -0.165747 -0.061057 -0.181863 -5.0 -4.0
2013-01-06 -0.205518 -1.796999 -1.640196 -5.0 -5.0
"""

# Faltan datos
# Para los tipos de datos NumPy, np.nan representa datos faltantes. Es por predeterminado
# no incluido en los cálculos. Ver el sección de Datos faltantes

# Reindexación le permite cambiar/agregar/eliminar el índica en un eje especifico. Esto devuelve
# una copia de los datos:

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ["E"])

df1.loc[dates[0]: dates[1], "E"] = 1

print(f'\n{df1}')
"""
Respuesta
                   A         B         C    D    F    E
2013-01-01  0.000000  0.000000 -0.165788  5.0  NaN  1.0
2013-01-02  0.814400 -0.025337  0.051152  5.0  1.0  1.0
2013-01-03  0.972725  0.565634 -1.736401  5.0  2.0  NaN
2013-01-04 -0.043997 -1.097054 -0.916392  5.0  3.0  NaN
"""

# DataFrame.dropna() deja caer cualquier fila que tenga datos faltantes:
print(f'\n{df1.dropna(how="any")}')
"""
Respuesta
                  A         B         C    D    F    E
2013-01-02 -0.10217  0.481892 -0.944989  5.0  1.0  1.0
"""

# DataFrame.fillna() rellena los datos faltantes:
print(f'\n{df1.fillna(value=5)}')
"""
Respuesta
                   A         B         C    D    F    E
2013-01-01  0.000000  0.000000  1.166674  5.0  5.0  1.0
2013-01-02  0.053495  0.730936  0.281658  5.0  1.0  1.0
2013-01-03  0.604803 -0.272974  1.269838  5.0  2.0  5.0
2013-01-04  1.468328 -1.336468  0.081799  5.0  3.0  5.0
"""

# isna() obtiene la máscara booleana donde están los valores nan
print(f'\n{pd.isna(df1)}')
"""
Respuesta
                A      B      C      D      F      E
2013-01-01  False  False  False  False   True  False
2013-01-02  False  False  False  False  False  False
2013-01-03  False  False  False  False  False   True
2013-01-04  False  False  False  False  False   True
"""

# Estadísticas
# Operaciones en general excluir datos faltantes

# Calcule el valor medio para cada columna
print(f'\n{df.mean()}')
"""
Respuesta
A    0.141247
B   -0.152348
C   -0.293673
D    5.000000
F    3.000000
dtype: float64
"""

# Calcule el valor medio para cada fila
print(f'\n{df.mean(axis=1)}')
"""
Respuesta
2013-01-01    0.809342
2013-01-02    1.592318
2013-01-03    2.129691
2013-01-04    1.402468
2013-01-05    2.503651
2013-01-06    1.172268
Freq: D, dtype: float64
"""

# Operando con otro Series o DataFrame con un índice o columna diferente alineará el resultado
# con la unión de las etiquetas de índice o columna. Además, pandas transmite automáticamente
# a lo largo de la dimensión especificada y llenará etiquetas no alineadas con np.nan

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
print(f'\n{s}')
"""
Respuesta
2013-01-01    NaN
2013-01-02    NaN
2013-01-03    1.0
2013-01-04    3.0
2013-01-05    5.0
2013-01-06    NaN
Freq: D, dtype: float64
"""

print(f'\n{df.sub(s, axis="index")}')
"""
Respuesta
                   A         B         C    D    F
2013-01-01       NaN       NaN       NaN  NaN  NaN
2013-01-02       NaN       NaN       NaN  NaN  NaN
2013-01-03 -1.263188 -0.425381 -0.421449  4.0  1.0
2013-01-04 -5.523332 -3.778178 -2.653856  2.0  0.0
2013-01-05 -4.761965 -7.018092 -6.703574  0.0 -1.0
2013-01-06       NaN       NaN       NaN  NaN  NaN
"""

# Funciones definidas por el Usuario
# DataFrame.agg() y DataFrame.transform() aplica una función definida por el usuario eso reduce
# o transmite su resultado respectivamente
print(f'\n{df.agg(lambda x: np.mean(x) * 5.6)}')
"""
Respuesta
A     0.755332
B     1.107438
C     3.298910
D    28.000000
F    16.800000
dtype: float64
"""

print(f'\n{df.transform(lambda x: x * 101.2)}')
"""
Respuesta
                     A          B           C      D      F
2013-01-01    0.000000   0.000000  -77.546615  506.0    NaN
2013-01-02  137.406294 -77.036773  154.649229  506.0  101.2
2013-01-03  -26.529994  -5.836422 -162.755525  506.0  202.4
2013-01-04   66.537815 -79.959120  -47.758614  506.0  303.6
2013-01-05    9.097833  72.279536  -46.827477  506.0  404.8
2013-01-06  -22.173602 -75.910030  -38.795828  506.0  506.0
"""

# Cuentas de Valor
# Ver más en Histogramación y Discretización
s = pd.Series(np.random.randint(0, 7, size=10))

print(f'\n{s}')
"""
Respuesta
0    5
1    3
2    1
3    5
4    0
5    4
6    5
7    6
8    4
9    4
dtype: int64
"""

print(f'\n{s.value_counts()}')
"""
Respuesta
5    3
4    3
3    1
1    1
0    1
6    1
Name: count, dtype: int64
"""


# Métodos de cuerda
# Series está equipado con un conjunto de métodos de procesamiento de cadenas en el
# str atributo que facilita el funcionamiento de cada elemento de la matriz, como en el
# fragmento de código a continuación. Ver más en Métodos de cuerda Vectorizada

s = pd.Series(["A", "B", "C", "Aaba", "Baca", np.nan, "CABA", "dog", "cat"])
print(f'\n{s.str.lower()}')
"""
Respuesta
0       a
1       b
2       c
3    aaba
4    baca
5     NaN
6    caba
7     dog
8     cat
dtype: object
"""

# Fusionar

# Concatenar
# Pandas ofrece varias instalaciones para combinar fácilmente Series y DataFrame objetos con
# varios tipos de lógica establecida para los índices y funcionalidad de álgebra relacional
# en el caso de unión/tipo fusión operaciones.

# Ver el sección de fusión

# Concatenar objetos de pandas juntos en cuanto a filas con concat()

df5 = pd.DataFrame(np.random.randn(10, 4))
print(f'\n{df5}')
"""
Respuesta
          0         1         2         3
0  1.250592 -0.233044  0.951094  0.398591
1 -1.529322 -1.000139  0.488478 -0.007104
2  1.925160  0.744334  1.332696 -0.955043
3  0.476547 -0.196675  2.896226 -0.132099
4 -0.843242  0.248651 -2.519125  0.429489
5 -1.802613  0.870560 -1.398827  0.640528
6 -1.043552  0.545058  0.595105  1.054205
7 -1.089379  1.049125 -0.913323 -0.773750
8 -0.775783 -1.261547  0.106367 -0.980901
9 -1.574588 -1.462179 -0.067068  0.359147
"""

# brek ir into pieces
pieces = [df5[:3], df5[3:7], df5[7:]]
print(f'\n{pd.concat(pieces)}')

# Nota
# Agregar una columna a un DataFrame es relativamente rápido. Sin embargo, agregando
# una fila requiere una copia y puede ser costosa. Recomendamos pasar a lista de registros
# preconstruida para el DataFrame constructor en su lugar de construir un DataFrame
# anexando iterativamente registros a él.

# Unificar
# merge() permite tipos de unión de estilo SQL a lo largo de columnas específicas. Ver el
# unión de estilo de base de datos sección

left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})

print(f'\n{left}')
"""
Respuesta
   key  lval
0  foo     1
1  foo     2
"""

print(f'\n{right}')
"""
Respuesta
   key  rval
0  foo     4
1  foo     5
"""

print(f'\n{pd.merge(left, right, on="key")}')
"""
Respuesta
   key  lval  rval
0  foo     1     4
1  foo     1     5
2  foo     2     4
3  foo     2     5
"""

# marge() unificar en llaves únicas:

left1 = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})
right1 = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})

print(f'\n{left1}')
"""
Respuesta
   key  lval
0  foo     1
1  bar     2
"""

print(f'\n{right1}')
"""
Respuesta
   key  rval
0  foo     4
1  bar     5
"""

print(f'\n{pd.merge(left1, right1, on="key")}')
"""
Respuesta
   key  lval  rval
0  foo     1     4
1  bar     2     5
"""

# Agrupación
# Por "group by" nos referimos a un proceso que involucra a uno o más de los pasos siguientes:
# · Dividiendo los datos en grupos basados en algunos criterios
# · Aplicando una función para cada grupo de forma independiente
# · Combinando los resultados en una estructura de datos

df6 = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)

print(f'\n{df6}')
"""
Respuesta
     A      B         C         D
0  foo    one -0.305530  0.644844
1  bar    one -0.255678  0.892210
2  foo    two  1.369921  1.082467
3  bar  three -0.079749  0.902532
4  foo    two  0.487012 -0.124013
5  bar    two  0.997006  0.937599
6  foo    one  0.433248  0.106527
7  foo  three -1.013924  0.299282
"""

# Agrupación para una etiqueta de columna, selección de etiquetas de columna y luego aplicación
# de la DataFrameGroupBy.sum() función al resultado grupos:

print(f'\n{df6.groupby("A")[["C", "D"]].sum()}')
"""
Respuesta
            C         D
A                      
bar -2.713273  0.482752
foo  2.996815  0.468895
"""

# Agrupación por múltiples columnas formularios de etiqueta MultiIndex

print(f'\n{df6.groupby(["A", "B"]).sum()}')
"""
Respuesta
                  C         D
A   B                        
bar one   -1.228361  1.318540
    three  0.843708 -0.388109
    two   -1.517024  0.428854
foo one   -1.300228  0.129348
    three  0.579920  1.037365
    two    0.816559  1.334073
"""
