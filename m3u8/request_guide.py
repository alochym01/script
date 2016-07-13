session = requests.session()
url = 'http://hdonline.vn/phim-freshwater-ho-quai-thu-12358.html'
r = session.get(url)
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
