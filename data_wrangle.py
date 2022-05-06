import pandas as pd
from typing import TextIO

def month_day_only(cell: str) -> str:
    str_cell = str(cell)
    return str_cell[0:6]

file = pd.read_csv('toronto_daily.csv', low_memory=False)
# file['LOCAL_DATE'] = file['LOCAL_DATE'].apply(month_day_only)
df = file['LOCAL_DATE'].str[0:5]

file.LOCAL_DATE = df.LOCAL_DATE

# df.to_csv('clean_toronto_daily.csv', sep='\t')

# def wrangle(input: TextIO) -> TextIO:
#     # reads the header line of the file
#     input.readline()

#     # reads each line of file
#     for line in input:
#         # only date and month
#         line[5] = line[5][0:5]
#     input.close()


# if __name__ == '__main__':
#     with open('toronto_daily.csv') as file:
#         wrangle(file)
