# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 03:20:33 2021

@author: Video Disdrometer
"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Dhananjay@13",
  database="dj"
)
#%%
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE dj")

mycursor.execute("CREATE TABLE audiofiles (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), duration int(11) unsigned, date DATETIME)")
#%%
#sql = "INSERT INTO customers (name, email,password) VALUES (%s, %s, %s)"
#val = ("Dhananjay", "dkadge@gmail.com", "Dhananjay@13")
#      
#mycursor.execute(sql, val)
#
#mydb.commit()
#for x in mycursor:
#  print(x)
#
#print(mycursor.rowcount, "record inserted.")
#print("Total record:", mycursor.lastrowid)
    

#%%
#from django.db import connections
#from django.db.utils import OperationalError
#db_conn = connections['default']
#try:
#    c = db_conn.cursor()
#except OperationalError:
#    connected = False
#else:
#    connected = True