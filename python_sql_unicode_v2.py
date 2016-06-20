#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode

db = mysql.connector.connect(user='root', password='abc@123', host='127.0.0.1', database='aloabc', use_unicode=True)
cursor = db.cursor()

sql = "select id, link from images where film_id=1"
cursor.execute(sql)

for (id, link) in cursor:
    print (link)

cursor.close()
db.close()
