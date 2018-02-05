# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 21:36:13 2018

@author: gabrieltenorio
"""

import os
import Reader as file
import Update as DB
import sqlite3

publishers = {}
for root, dirs, files in os.walk("/Users/gabrieltenorio/desktop/files/Planilhas-Subir-Vendas-lucas/"):
    for d in dirs:
        folder =os.path.join(d)
        for root, dirs, files in os.walk("/Users/gabrieltenorio/desktop/files/Planilhas-Subir-Vendas-lucas/"+folder):
            publishers[folder] = files
            
try:
    conn = sqlite3.connect('dataBase.db')
except Exception as e:
    print(e)
    
for key in publishers:
    for i in range(len(publishers[key])):
        x = ''
        path = "/Users/gabrieltenorio/desktop/files/Planilhas-Subir-Vendas-lucas/" + key +'/'+ publishers[key][i]
        row = file.readRows(path) 
        row.append(key) # Nome da pasta
        row.append(publishers[key][i].split('.')[0])
        DB.updateDb(row)