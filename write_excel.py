#encoding = utf-8
from xlrd import open_workbook
from xlutils.copy import copy
file = 'C:\\Users\\lyancoffee\\Desktop\\apitest\\api_case.xlsx'
rb = open_workbook(file)
 

rs = rb.sheet_by_index(0)
 
wb = copy(rb)
 

ws = wb.get_sheet(0)
ws.write(1,5,'changed!')
 
wb.save(file)