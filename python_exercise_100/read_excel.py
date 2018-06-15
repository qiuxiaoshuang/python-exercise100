import xlrd
# 读取的文件路径
file_path= r'C:/Users/xiong/Desktop/qiuxiaoshuang1/python_exercise_100/字符串函数（180615）.xlsx'
# 文件中的中文转码# 获取数据
data = xlrd.open_workbook(file_path)
# 获取sheet
table = data.sheet_by_name('string字符串函数')
# 获取总行数
nrows = table.nrows
print(nrows)
# 获取总列数
ncols = table.ncols
print(ncols)
# 输出数据
for i in range(0,nrows):
    rowValues= table.row_values(i) #某一行数据
    for item in rowValues:
        print (item)
# table.row_values(i)
# # 获取一行的数值
# table.col_values(i)
# #
#
# # 获取一个单元格的数值
# cell_value = table.cell(a,b).value