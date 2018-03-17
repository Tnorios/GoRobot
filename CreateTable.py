# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:29:36 2018

@author: Administrator
"""

import sqlite3
from pathlib import Path


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
 
    return None

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)
        

def createTable():
   database = "dataBase.db"
   table = """ CREATE TABLE dataBase(
               publisher VARCHAR(100) NOT NULL,
               advertiser INT(10) NOT NULL,
               advertiserName VARCHAR(100) NOT NULL,
               publisherEmail VARCHAR(100) NOT NULL,
               partnerId VARCHAR(100) NOT NULL,
               PRIMARY KEY (publisher, advertiser)
               );"""
   
   conn = create_connection(database)
   if conn is not None:
       create_table(conn, table)
