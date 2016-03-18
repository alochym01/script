# -*- coding: utf-8 -*-
import MySQLdb
import json


files = ["/home/hadn/script/tuoitre_crawler/tuoitre/1063441/1063441.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1063462/1063462.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1063576/1063576.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1063726/1063726.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1063762/1063762.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1063768/1063768.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1063792/1063792.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1063795/1063795.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1063822/1063822.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1063951/1063951.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1064119/1064119.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1064134/1064134.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1064293/1064293.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1064344/1064344.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1064383/1064383.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1064449/1064449.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1064452/1064452.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1064542/1064542.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1064548/1064548.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1064605/1064605.html",
         "/home/hadn/script/tuoitre_crawler/tuoitre/1064731/1064731.html"
         ]
db = MySQLdb.connect("localhost", "root", "abc@123", "yii2basic", use_unicode=True, charset="utf8")
cursor = db.cursor()

for i in files:
    with open(i) as f:
        data = json.loads(f.read())
        print type(data['items'][0]['snippet']['description'])
        sql = "insert into news(title, description, cateid, slug, img_small, img_standard, source) values('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (data['items'][0]['snippet']['title'], unicode(data['items'][0]['snippet']['description']), "xa-hoi", data['items'][0]['etag'], data['items'][0]['snippet']['thumbnails']['default']['url'], data['items'][0]['snippet']['thumbnails']['standard']['url'], 'tuoitre')
        sqlcate = "insert into categories(url, name, code) values('%s', '%s', '%s')" % (data['items'][0]['snippet']['url'], "Xa Hoi", "xa-hoi")
    print sql
    cursor.execute(sql)
    cursor.execute(sqlcate)
    db.commit()
