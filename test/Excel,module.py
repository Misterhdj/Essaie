
from openpyxl import *
import openpyxl
workbook = openpyxl.load_workbook('LexiqueNew.xlsx')
wb = Workbook('LexiqueNew.xlsx')

# grab the active worksheete
ws = wb.active

# Data can be assigned directly to cells
ws['A1'] = 42

# Rows can also be appended
ws.append([1, 2, 3])

# Python types will automatically be converted
import datetime
ws['A2'] = datetime.datetime.now()

# Save the file
wb.save("sample.xlsx")