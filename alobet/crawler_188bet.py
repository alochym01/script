import requests
import json
from datetime import datetime
import redis
import sys
import os
'''
league_list = '{"euro_2016":"Euro 2016","copa_american":"Copa America Centenario 2016 (In USA)"}'
r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.set("league_list", league_list)
d = json.loads(league_list)
leagues_188_params = '{"euro_2016":{"payload":{"ifl":true,"ipf":false,"iip":false,"pn":0,"tz":420,"pt":2,"pid":262,"sid":[1],"ubt":"am","dc":null,"dv":-1,"ot":0}},\
        "copa_american":{"payload":{"ifl":true,"ipf":false,"iip":false,"pn":0,"tz":420,"pt":2,"pid":0,"sid":[1],"ubt":"am","dc":-2,"dv":0,"ot":2,"sb":1,"cid":["57936"]}}\
                        }'
dparams = json.loads(leagues_188_params)
for k,v in d.items():
    print 'crawing for %s' % (k)
    os.system("python /alobet68/public/crawler_188bet_league.py %s '%s'" % (k,json.dumps(dparams[k]['payload'])))
    print 'crawed for %s' % (k)
'''
payload = 'IsFirstLoad=true&VersionL=-1&VersionU=0&VersionS=-1&VersionF=-1&VersionH=1%3A0%2C2%3A0%2C3%3A0%2C4%3A0%2C7%3A0%2C14%3A0%2C21%3A0%2C23%3A0&VersionT=-1&IsEventMenu=false&SportID=1&CompetitionID=-1&reqUrl=%2Fvi-vn%2Fsports%2Ffootball%2Fmatches-by-date%2Ftoday%2Ffull-time-asian-handicap-and-over-under%3Fcompetitionids=38741&oIsInplayAll=false&oIsFirstLoad=true&oSortBy=1&oOddsType=0&oPageNo=0'
os.system("python /mnt/crawler_188bet/crawler_188bet_league_cs.py '%s'" % (payload))

