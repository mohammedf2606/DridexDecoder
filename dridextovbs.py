import sys
import pandas as pd
from itertools import chain
import click


# Filter rows depending on if there is number
def filter_row(in_row):
    in_row = in_row[~pd.isna(in_row)]
    return in_row


def process(in_file, offset):
    file_loc = in_file

    data = pd.DataFrame()
    extension = file_loc.split(".")[-1]

    if extension == "xlsb":
        data = pd.read_excel(file_loc, engine="pyxlsb")
    elif extension == "csv":
        data = pd.read_csv(file_loc)
    elif extension == "xls":
        data = pd.read_excel(file_loc, engine="xlrd")
    else:
        data = pd.read_excel(file_loc)

    np_array = data.values
    empty_rows = []
    filtered_array = []

    for index, row in enumerate(np_array):
        filtered = filter_row(row)
        if filter_row(row).size == 0:
            empty_rows.append(index)
        filtered_array.append(filtered.tolist())

    # Join rows together as a single list
    # Finds the last empty row before the content and selects all rows after that
    decimal_nums = list(chain(*chain(*[filtered_array[empty_rows[-1] + 1:]])))

    final_script = ""
    for num in decimal_nums:
        final_script += chr(int(num) + offset)

    return final_script


@click.command()
@click.option("--in", "-i", "in_file", required=True, type=click.Path(),
              help="Path to Excel file to be processed.")
@click.option("--offset", "-f", show_default=True, default=0,
              help="Offset to add to or subtract from values (specify minus for negative)")
@click.option("--std-out", "-s", is_flag=True,
              help="Output to the command line")
@click.option("--verbose", "-v", is_flag=True,
              help="Print output to console")
def main(in_file, offset, std_out, verbose):
    script = process(in_file, offset)
    if std_out:
        print(script)
        sys.stdout.write(script)
    elif verbose:
        print(script)


if __name__ == '__main__':
    main()
