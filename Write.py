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


def write(sales):
    sales.sort()
    print(sales)
    print('')
    progs = {}
    date = time.strftime("%Y-%m-%d")
    DatePath = '/Users/gabrieltenorio/desktop/files//Arquivos-'+date
    if not os.path.exists(DatePath):
        os.makedirs(DatePath)

    for i in range(0,(len(sales))):
        if sales[i][0] in progs:
            progs[sales[i][0]].append(sales[i])     
        else:
            progs[sales[i][0]] = [sales[i]]
        
    
    for key, values in progs.items():
        with open(DatePath+'/'+key+'-'+date + '.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, dialect='excel', delimiter=';')
            writer.writerow(['prog_id','time_stamp','order_id','customer_id','currency_symbol','total_price','review_state','review_note','partner_id','tracking_type','update_flag'])
            print('')
            order = []
            for data in values:         
                if data[2] in order:
                    pass
                else:
                    order.append(data[2])
                    line = []
                    ProgID = DB.getProgID(key)
                    if (ProgID == 0):
                        print("program ID error", key)
                        break
                    else:
                        Fdate  = time.strftime("%Y-%m-%d" + " 10:00:00")
                        if not(isinstance(data[-1], str)):
                            seconds = (data[1] - 25569) * 86400.0
                            reviewNote = (datetime.datetime.utcfromtimestamp(seconds))
                        else:
                            reviewNote = data[-1]
                        PartnerId = DB.getPartnerId(ProgID, 'meliuz@zanox.com')
                        line.extend((ProgID, Fdate, str(data[2]), 'meliuz@zanox.com', 'BRL', float(data[3]), 0 ,str(reviewNote),PartnerId,3,4 ))
                        print(line)
                        writer.writerow(line)
                
    
        
        
        
                

write([['Teste', '12-01-2018', 32423412.0, '423'],['Teste', '12-01-2018', 3242343412.0, '423'],['123 Milhas', 430536.0, '7O1-M0K-17', 2450.44],['Nescafé Dolce Gusto',43036.0, 5501915888.0, 646.0],['Monte Carlo Joias',43036.0, '7729406525580-01', 42.0],  ['Nescafé Dolce Gusto',43036.0, 5501915888.0, 666.0],['Monte Carlo Joias',43036.0, '772940652580-01', 142.0], ['Motorola',43036.0, '01-64886397', 1300.0],['Monte Carlo Joias',43036.0, '772940623452580-01', 96.0]])
