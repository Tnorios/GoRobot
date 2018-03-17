# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:36:13 2018

@author: gabrieltenorio
"""

import os
import Reader as file
import Update as DB
import CreateTable as ct

publishers = {}
for root, dirs, files in os.walk("C:/Users/gabriel.tenorio/Desktop/GoRobot-master/Planilhas-Subir-Vendas-lucas/"):
    for d in dirs:
        folder =os.path.join(d)
        for root, dirs, files in os.walk("C:/Users/gabriel.tenorio/Desktop/GoRobot-master/Planilhas-Subir-Vendas-lucas/"+folder):
            publishers[folder] = files
    
ct.createTable()

    
for key in publishers:
    for i in range(len(publishers[key])):
        path = "C:/Users/gabriel.tenorio/Desktop/GoRobot-master/Planilhas-Subir-Vendas-lucas/" + key +'/'+ publishers[key][i]
        row = file.readRows(path) 
        row.append(key) # Nome da pasta
        row.append(publishers[key][i].split('.')[0])
        DB.updateDb(row)