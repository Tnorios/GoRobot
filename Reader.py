# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 22:03:43 2018

@author: gabrieltenorio
"""

import os.path
import csv

def readRows(file):
    data = []
    with open(os.path.abspath(file),encoding='ISO-8859-1') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',', )
        string = str(csvfile).split("/")[-1]
        try:
            lista = list(readCSV)
            for row in range(2): 
                warning = 0
                row = (lista[row][0].split(';'))
                if(len(row) < 11):
                    print(string)
                    raise Exception('Verificar os indices do seguinte arquivo:')
                else:
                    for i in range(len(row)):
                        if(row[i] == ''):
                            warning += 1
                    if(warning > 2):
                        raise Exception('Verificar os dados o seguinte arquivo:')
                    else:
                        data.append(row)
        except Exception as e:
            print("Erro: ",e,string.split("mode")[0],end='')     
        for i in range(1,(len(data))):
            for j in range(0,len(data)-1):
                #print('(',i,"&",j,')')
                if(len(data[i]) != len(data[j])):
                    raise Exception('Verificar as virgulas o do seguinte arquivo',csvfile)
        return data