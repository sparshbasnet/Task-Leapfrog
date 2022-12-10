from openpyxl import Workbook, load_workbook
import pandas as pd 
wb = load_workbook('test.xlsx')
ws = wb.active

df = pd.DataFrame(ws.values, columns = ['Name', 'id', 'science', 'maths', 'English', 'Remarks'])

new_df = df.iloc[1:]
pass_mark = 50

print(new_df[(new_df['maths'] < pass_mark ) & (new_df['science'] < pass_mark )])