#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 19:33:25 2018

@author: gabrieltenorio
"""

import sqlite3
import difflib


def updateDb(line):
    conn = sqlite3.connect('dataBase.db')
    cursor = conn.cursor()
    sqlQuery = ''
    try:
        pub = line[-2]
        adv = line[-1]
        line = line[1]
        cursor.execute("SELECT publisher, advertiser FROM database WHERE publisher='{}' and advertiser='{}'".format(pub, int(line[0])));
        dataQuery = cursor.fetchall()
        if(len(dataQuery)!=0):
            pass
        else:
            sqlQuery = "INSERT INTO database VALUES ('{}',{},'{}','{}','{}');".format(pub, int(line[0]), adv, line[3].lower(), line[8])
            cursor.execute(sqlQuery)
            conn.commit()
            conn.close()
    except Exception as e:
        if(sqlQuery):
            print('Erro ao atualizar o banco na query:',sqlQuery,e)
        else: 
            print('')
        
        
def printDB():
    try:
        conn = sqlite3.connect('dataBase.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM database")
        for linha in cursor.fetchall():
            print(linha)
    except Exception as e:
        print(e)
        
def getProgID(progID):
    x = []
    conn = sqlite3.connect('dataBase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT advertiserName FROM dataBase;")
    for item in cursor.fetchall():
        x.append(item)
    l = []
    for i in range(len(x)):
        l.append(x[i][0])
    try:
        name  = (difflib.get_close_matches(progID, l))[0]
    except:
        return 0
    cursor.execute("SELECT advertiser FROM dataBase WHERE advertiserName = '{}' ;".format(name))
    return cursor.fetchall()[0][0]

def getPartnerId(progID, publisher ):
    conn = sqlite3.connect('dataBase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT partnerId FROM dataBase WHERE advertiser = '{}' and publisherEmail='{}' ;".format(progID, publisher))
    try:
        return cursor.fetchall()[0][0]
    except:
        return 0
    


    