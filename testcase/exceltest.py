#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取excel数据
# 小罗的需求，取第二行以下的数据，然后取每行前13列的数据
import xlrd
data = xlrd.open_workbook('D:\\readExcel.xlsx') # 打开xls文件
# print (data.sheet_names())
sheet = data.sheet_by_name('test')
# rows = sheet.row_values(1) # 获取第四行内容
# cols = sheet.col_values(1) # 获取第三列内容
# print (rows)
# print (cols)


# inputValue=sheet.cell_value(1,1)
# if isinstance(inputValue,float):    #判断读取到的值是否为float
#     if inputValue==int(inputValue): #判断读取到的值与转成int后的值是否相等，如果相等则转成int
#         inputValue = int(inputValue)
#     inputValue = str(inputValue) #转成str



Value=sheet.cell_value(1,1)
xx=Value.isinstance()
print(xx)

def isinstance(inputValue,float):
    if inputValue==int(inputValue): #判断读取到的值与转成int后的值是否相等，如果相等则转成int
        inputValue = int(inputValue)
    inputValue = str(inputValue) #转成str
    return inputValue