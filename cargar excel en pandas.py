import pandas

data_frame = pandas.read_excel(
    "Archivos adicionales/supermarkets.xlsx", sheet_name=0)

print(data_frame)
