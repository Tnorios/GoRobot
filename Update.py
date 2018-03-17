#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 19:33:25 2018

@author: gabrieltenorio
"""
 #[['prog_id', 'time_stamp', 'order_id', 'customer_id', 'currency_symbol', 'total_price', 'review_state', 'review_note', 'partner_id', 'tracking_type', 'update_flag'], ['15900', '2018-02-09 10:00:00', '20557976', 'operacional@risu.com.br', 'BRL', '109.8', '0', 'b13aafdd-dcd6-4419-a3e2-a691008a6e89', '30839742C66693734', '3', '4'], 'Risu', 'Zattini']
import sqlite3
import difflib


def updateDb(line):
    conn = sqlite3.connect('dataBase.db')
    cursor = conn.cursor()
    sqlQuery = ''
    try:    
        pub = line[-2]
        adv = line[-1].lower()
        line = line[1]
        cursor.execute("SELECT publisher, advertiser FROM dataBase WHERE publisher='{}' and advertiser='{}'".format(pub, int(line[0])));
        dataQuery = cursor.fetchall()
        if(len(dataQuery)!=0):
            pass
        else:
            sqlQuery = "INSERT INTO dataBase VALUES ('{}',{},'{}','{}','{}');".format(pub, int(line[0]), adv, line[3].lower(), line[8])
            cursor.execute(sqlQuery)
            conn.commit()
            conn.close()
    except Exception as e:
        if(sqlQuery):
            print('Erro ao atualizar o banco na query:',sqlQuery,e)

        
        
def printDB():
    try:
        conn = sqlite3.connect('dataBase.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dataBase ")
        for linha in cursor.fetchall():
            print(linha)
    except Exception as e:
        print(e)
        
def getProgID(progID):
    x = []
    progID = progID.lower()
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

def getAdvId(prog):
    conn = sqlite3.connect('dataBase.db')
    cursor = conn.cursor()
    cursor.execute("SELECT advertiserName FROM dataBase WHERE advertiser = '{}' ;".format(prog))
    try:
        return cursor.fetchall()[0][0]
    except:
        return 0
    

#def insertNewAdv(adv):  
#    conn = sqlite3.connect('dataBase.db')
#    cursor = conn.cursor()
#    sqlQuery = ''
#
#    
#    advID = getAdvId(adv)
#    if (advID != 0):
#        print(getPartnerId(advID, 'meliuz@zanox.com'))
#        print("erro",advID)
        #Inserir informações 
#    try:
#        cursor.execute("SELECT publisher, advertiser FROM dataBase WHERE publisher='{}' and advertiser='{}'".format(pub, int(line[0])));
#        dataQuery = cursor.fetchall()
#        if(len(dataQuery)!=0):
#            pass
#        else:
#            sqlQuery = "INSERT INTO dataBase VALUES ('{}',{},'{}','{}','{}');".format(pub, int(line[0]), adv, line[3].lower(), line[8])
#            cursor.execute(sqlQuery)
#            conn.commit()
#            conn.close()
#    except Exception as e:
#        if(sqlQuery):
#            print('Erro ao atualizar o banco na query:',sqlQuery,e)
    

#insertNewAdv(14929)