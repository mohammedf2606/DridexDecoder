import pandas as pd
import numpy as np
import re

file_loc = "/home/remnux/Downloads/dridex.xlsb"
# file_loc = "/home/remnux/Downloads/d3bf39bbba7b499e7cc2e20a2986a95164376b2331c1493fd280a467c49d773c.xlsx"

data = pd.DataFrame()
extension = file_loc.split(".")[-1]
print(extension)


if extension == "xlsb":
    data = pd.read_excel(file_loc, engine="pyxlsb")
elif extension == "csv":
    data = pd.read_csv(file_loc)
elif extension == "xls":
    data = pd.read_excel(file_loc, engine="xlrd")
else:
    data = pd.read_excel(file_loc)


# Filter rows depending on if there is number
def filter_row(in_row):
    in_row = in_row[~pd.isna(in_row)]
    print(in_row)

    # row_string = str(in_row)
    # row_string = row_string.replace("nan", "").replace("\n", "").replace("[", "").replace("]", "")
    # split = np.array(row_string.split(" "))
    # unique_rows = np.unique(split)
    # without_empty_str = np.delete(unique_rows, np.where(unique_rows == ''))
    #
    # pattern = "^'([0-9]+)(.0)?'$"
    # print(without_empty)
    # is_match = re.match(pattern, str(without_empty))
    # if is_match is None:
    #     return None
    # print(is_match)


np_array = data.values
rows_with_nums = []
for index, row in enumerate(np_array):
    if filter_row(row) is not None:
        rows_with_nums.append(row)
# print(rows_with_nums)

