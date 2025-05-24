import pandas

data_frame = pandas.read_excel(
    "Archivos csv txt xlsx y zip/supermarkets.xlsx", sheet_name=0)

print(data_frame)
