import feedparser

url = 'http://ictnews.vn/rss/internet'

feed = feedparser.parse(url)
# keys = ['feed',
#        'status',
#        'version',
#        'encoding',
#        'bozo',
#        'headers',
#        'href',
#        'namespaces',
#        'entries',
#        'bozo_exception']

for item in feed['entries']:
    print item.link
    print item.title
    print item.summary
    print item.published
