#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 22:19:23 2018

@author: gabrieltenorio
"""
import Write as w
import xlrd as excel
import os.path
columns = []
values = []
data = []

file = "/Users/gabrieltenorio/desktop/files/Teste1.xlsx"
files = excel.open_workbook(os.path.abspath(file))
pl = files.sheet_by_index(0)
for column in range(pl.ncols):
    index = pl.col_values(column)[0]
    if(index == "PEDIDO" or  index =="LOJA" or index =="VALOR" or index=="DATA"):
        columns.append(column)
for i in range (1, len(pl.col_values(column))):
    for j in columns:        
        values.append(pl.row_values(i)[j])
    data.append(values)
    values = []

w.write(data)
       
    
            