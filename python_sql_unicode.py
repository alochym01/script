import re
import MySQLdb

db = MySQLdb.connect("localhost","root","abc@123","yii2basic", use_unicode=True, charset="utf8")
cursor = db.cursor()

for i in files:
     with open(i) as f:
        data = json.loads(f.read())
        sql = "insert into items(videoid, publishedat, title, thumbnails, tag, description, channelid) values('%s', '%s', '%s', \"%s\", '%s', '%s', '%s')" % (data["items"][0]["id"], data["items"][0]["snippet"]["publishedAt"], re.sub("'", "", data["items"][0]["snippet"]["title"]"'"), str(data["items"][0]["snippet"]["thumbnails"]), data["items"][0]["snippet"]["tags"][0], re.sub("'", "", data["items"][0]["snippet"]["description"]"'"), data["items"][0]["snippet"]["channelId"])
            print sql
            cursor.execute(sql)
            db.commit()


