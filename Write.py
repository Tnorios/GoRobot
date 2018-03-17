#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 21:45:09 2018

@author: gabrieltenorio
"""

import csv
import Update as DB
import time
import datetime
import os.path
import main


def write(sales, output):
    errorLog = []
    progs = {}
    date = time.strftime("%Y-%m-%d")
    DatePath = output+'/'+date
    print(DatePath)
    if not os.path.exists(DatePath):
        os.makedirs(DatePath)

    for i in range(0,(len(sales))):
        if sales[i][0] in progs:
            progs[sales[i][0]].append(sales[i])     
        else:
            progs[sales[i][0]] = [sales[i]]
        
    
    for key, values in progs.items():
        with open(DatePath+'/'+key+'-'+date + '.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, dialect='excel', delimiter=';')
            writer.writerow(['prog_id','time_stamp','order_id','customer_id','currency_symbol','total_price','review_state','review_note','partner_id','tracking_type','update_flag'])
            order = []
            for data in values:     
                if data[2] in order:
                    pass
                else:
                    if(isinstance(data[2],float)):
                        data[2] = int(data[2])
                    order.append(data[2])
                    line = []
                    ProgID = DB.getProgID(key)
                    if (ProgID == 0):
                        errorID = ("Couldn't find the program ID for: "+str(key))
                        errorLog.append(errorID)
                        #main.idNotFound(error)
                        break
                    else:
                        Fdate  = time.strftime("%Y-%m-%d" + " 10:00:00")
                        if not(isinstance(data[1], str)):
                            seconds = (data[1] - 25569) * 86400.0
                            reviewNote = (datetime.datetime.utcfromtimestamp(seconds))         
                            reviewNote = str(reviewNote)[:10]
                        else:
                            reviewNote = data[1]
                        PartnerId = DB.getPartnerId(ProgID, data[4])
                        if(PartnerId ==0):
                             errorPID = ("Couldn't find the Partner ID for: "+str(key)+" and "+ str(data[4]))
                             errorLog.append(errorPID)
                             break
                             #main.idNotFound(error)        
                        line.extend((ProgID, Fdate, str(data[2]), data[4], 'BRL', float(data[3]), 0 ,reviewNote,PartnerId,3,4 ))
                        try:
                            writer.writerow(line)
                        except Exception as e:
                            errorLog.append(e)
    return errorLog
                        
    
        
        
        
                

