import requests
import json
from datetime import datetime
import redis
import sys

host='sb.188bet.com'
#geturi='/vi-vn/programme/football/262/competition/correct-score'
craw_post_uri='/vi-vn/Service/CentralService?GetData'
update_ot_uri='/vi-vn/Service/OddsService?UpdateOddsType&OddsType=2'
def getValue(dict, v, i):
    if v in dict:
        return dict[v][i]
    else:
        return ''

def getAHValue(v):
    if v:
        if v[:1] == '-':
            return '0'
        else:
            if v[:1] == '+':
                v = v[1:]
            nums = v.split('/')
            if len(nums) == 2:
                v = str((float(nums[0]) + float(nums[1]))/2);
            else:
                v = nums[0]
    return v

def getOUTotalGoals(v):
    if v:
        nums = v.split('/')
        if len(nums) == 2:
            v = str((float(nums[0]) + float(nums[1]))/2);
        else:
            v = nums[0]
    return v
session = requests.session()
r = session.get('https://%s' % (host))
print r.status_code
session.headers.update({'Referer':'https://%s/vi-vn/sports/football/matches-by-date/today/full-time-asian-handicap-and-over-under'%(host)})
#session.get('https://%s%s' % (host, update_ot_uri))
cookie_val = {}
cookie_val['timeZone'] = '420'
cookie_val['settingProfile'] = 'OddsType%3D2'
requests.utils.add_dict_to_cookiejar(session.cookies,cookie_val)
#print r.status_code
session.headers.update({'content-type':'application/x-www-form-urlencoded'})
#hongkong ot = 2
#payload = '{"ifl":true,"ipf":false,"iip":false,"pn":0,"tz":420,"pt":1,"pid":0,"sid":[1],"ubt":"am","dc":null,"dv":0,"ot":2,"sb":1,"cid":["27166"]}'
if  len(sys.argv) < 2:
    sys.exit('missing payload')
payload = sys.argv[1]
print payload
post_url = 'https://%s%s' % (host,craw_post_uri)
print post_url
r = session.post(post_url, payload)
print r.status_code
#print r.text
dict = json.loads(r.text)
#print inplay
match_template_json = '{\
        "update_time": "%s",\
        "match_time": "%s",\
        "firsthalf": {\
        "asia": {\
        "asia_home_handicap": "%s",\
        "asia_away_handicap": "%s",\
        "asia_home_win_multiplier": "%s",\
        "asia_away_win_multiplier": "%s"\
        },\
        "eu" : {\
        "eu_home_win_multiplier": "%s",\
        "eu_away_win_multiplier": "%s",\
        "eu_draw_multiplier": "%s"\
        },\
        "ou" : {\
        "ou_numberofgoals": "%s",\
        "ou_over_win_multiplier": "%s",\
        "ou_under_win_multiplier": "%s"\
        },\
        "score" : {"1 - 0":"%s","0 - 1":"%s","2 - 0":"%s","0 - 2":"%s","2 - 1":"%s","1 - 2":"%s",\
                "3 - 0":"%s","0 - 3":"%s","3 - 1":"%s","1 - 3":"%s","3 - 2":"%s","2 - 3":"%s",\
                        "0 - 0":"%s","1 - 1":"%s","2 - 2":"%s","3 - 3":"%s"}\
        },\
        "fulltime": {\
        "asia": {\
        "asia_home_handicap": "%s",\
        "asia_away_handicap": "%s",\
        "asia_home_win_multiplier": "%s",\
        "asia_away_win_multiplier": "%s"\
        },\
        "eu" : {\
        "eu_home_win_multiplier": "%s",\
        "eu_away_win_multiplier": "%s",\
        "eu_draw_multiplier": "%s"\
        },\
        "ou" : {\
        "ou_numberofgoals": "%s",\
        "ou_over_win_multiplier": "%s",\
        "ou_under_win_multiplier": "%s"\
        },\
        "score" : {"1 - 0":"%s","0 - 1":"%s","2 - 0":"%s","0 - 2":"%s","2 - 1":"%s","1 - 2":"%s",\
        "3 - 0":"%s","0 - 3":"%s","3 - 1":"%s","1 - 3":"%s","3 - 2":"%s","2 - 3":"%s",\
        "4 - 0":"%s","0 - 4":"%s","4 - 1":"%s","1 - 4":"%s","4 - 2":"%s","2 - 4":"%s","4 - 3":"%s",\
        "3 - 4":"%s","0 - 0":"%s","1 - 1":"%s","2 - 2":"%s","3 - 3":"%s","4 - 4":"%s"}\
        }\
        }'

dleagues = dict['mod']['d'][0]['c']
r = redis.StrictRedis(host='localhost', port=6379, db=0)
league_list = {}
for league in dleagues:
    league_name = league['n']
    print 'league name%s' % (league['n'])
    dmatchs = league['e']
    matchs_bet_data = {}
    for match in dmatchs:
        if match['cei']['ctid'] == 0:
            match_name = match['i'][0] + ' vs ' + match['i'][1]
            print 'crawing for %s' % match_name
            match_json = match_template_json % (
                datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
                match['i'][4] + ' ' + match['i'][5] + ' ' + match['i'][12],
                getAHValue(getValue(match['o'],'ah1st',1)),
                getAHValue(getValue(match['o'],'ah1st',3)),
                getValue(match['o'],'ah1st',5),
                getValue(match['o'],'ah1st',7),
                getValue(match['o'],'1x21st',1),
                getValue(match['o'],'1x21st',3),
                getValue(match['o'],'1x21st',5),
                getOUTotalGoals(getValue(match['o'],'ou1st',1)),
                getValue(match['o'],'ou1st',5),
                getValue(match['o'],'ou1st',7),
                getValue(match['o'],'cs1st',1),
                getValue(match['o'],'cs1st',3),
                getValue(match['o'],'cs1st',5),
                getValue(match['o'],'cs1st',7),
                getValue(match['o'],'cs1st',9),
                getValue(match['o'],'cs1st',11),
                getValue(match['o'],'cs1st',13),
                getValue(match['o'],'cs1st',15),
                getValue(match['o'],'cs1st',17),
                getValue(match['o'],'cs1st',19),
                getValue(match['o'],'cs1st',21),
                getValue(match['o'],'cs1st',23),
                getValue(match['o'],'cs1st',25),
                getValue(match['o'],'cs1st',27),
                getValue(match['o'],'cs1st',29),
                getValue(match['o'],'cs1st',31),
                getAHValue(getValue(match['o'],'ah',1)),
                getAHValue(getValue(match['o'],'ah',3)),
                getValue(match['o'],'ah',5),
                getValue(match['o'],'ah',7),
                getValue(match['o'],'1x2',1),
                getValue(match['o'],'1x2',3),
                getValue(match['o'],'1x2',5),
                getOUTotalGoals(getValue(match['o'],'ou',1)),
                getValue(match['o'],'ou',5),
                getValue(match['o'],'ou',7),
                getValue(match['o'],'cs',1),
                getValue(match['o'],'cs',3),
                getValue(match['o'],'cs',5),
                getValue(match['o'],'cs',7),
                getValue(match['o'],'cs',9),
                getValue(match['o'],'cs',11),
                getValue(match['o'],'cs',13),
                getValue(match['o'],'cs',15),
                getValue(match['o'],'cs',17),
                getValue(match['o'],'cs',19),
                getValue(match['o'],'cs',21),
                getValue(match['o'],'cs',23),
                getValue(match['o'],'cs',25),
                getValue(match['o'],'cs',27),
                getValue(match['o'],'cs',29),
                getValue(match['o'],'cs',31),
                getValue(match['o'],'cs',33),
                getValue(match['o'],'cs',35),
                getValue(match['o'],'cs',37),
                getValue(match['o'],'cs',39),
                getValue(match['o'],'cs',41),
                getValue(match['o'],'cs',43),
                getValue(match['o'],'cs',45),
                getValue(match['o'],'cs',47),
                getValue(match['o'],'cs',49),
            )
            #print match_json
            print '%s crawed successfully' % match_name
            matchs_bet_data[match_name] = json.loads(match_json)
    #print matchs_bet_data;
    league_list[league_name] = league_name
    result = {}
    result[league_name] = matchs_bet_data
    r.set(league_name, json.dumps(result))
    r.expire(league_name, 3620)
r.set('league_list', json.dumps(league_list))
