import xlwt
f = xlwt.Workbook() 
sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) 
l_=[1,2,3,4,5]
for i in range(len(l_)):
    sheet1.write(6,i,i)
f.save('C:\Users\lyancoffee\Desktop\\tt.xls')