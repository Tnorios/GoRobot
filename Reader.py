# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 22:03:43 2018

@author: gabrieltenorio
"""
import os.path
import csv
import Write as w
import xlrd as excel
from tkinter import messagebox


def readRows(file):
    data = []
    folder = file.split("/")[-2]
    with open(os.path.abspath(file), encoding='ISO-8859-1') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',', )
        string = str(csvfile).split("\\")[-1]
        try:
            lista = list(readCSV)
            for row in range(2):
                warning = 0
                row = (lista[row][0].split(';'))
                if (len(row) < 11):  
                    raise Exception('Verificar os indices do seguinte arquivo:')
                else:
                    for i in range(len(row)):
                        if (row[i] == ''):
                            warning += 1
                    if (warning > 2):
                        raise Exception('Verificar os dados o seguinte arquivo:')
                    else:
                        data.append(row)
        except Exception as e:
            print(e, string.split("mode")[0], "da pasta", folder)
        for i in range(1, (len(data))):
            for j in range(0, len(data) - 1):
                # print('(',i,"&",j,')')
                if (len(data[i]) != len(data[j])):
                    raise Exception('Verificar as virgulas o do seguinte arquivo', csvfile)
        return data
    
def readMainFile(path, output):
    columns = []
    values = []
    data = []
    try:
        files = excel.open_workbook(os.path.abspath(path))
    except Exception as e:
        print(e)
    pl = files.sheet_by_index(0)
    for column in range(pl.ncols):
        index = pl.col_values(column)[0]
        if(index == "PEDIDO" or  index =="LOJA" or index =="VALOR" or index=="DATA" or index=="PUBLISHER"):
            columns.append(column)
    if(len(columns) != 5):
        return(messagebox.showerror("Erro", "Check the index in the main file"))
    else:
        for i in range (1, len(pl.col_values(column))):
            for j in columns:        
                values.append(pl.row_values(i)[j])
            data.append(values)
            values = []
        
        errorLog = w.write(data, output)
        if (errorLog == []):
            return(messagebox.showinfo("Successful", "All files have been created"))
        else:
            x=""
            for e in errorLog:
                x += (str(e)+'\n' )
            return(messagebox.showwarning("Please check the following errors", x))


