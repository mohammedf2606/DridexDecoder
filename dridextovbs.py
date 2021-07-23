import pandas as pd

file_loc = input("File path (give full path): ")

extension = file_loc.split(".")[-1]
print(extension)

data = pd.read_excel(file_loc, engine="pyxlsb")
print(data.shape)

