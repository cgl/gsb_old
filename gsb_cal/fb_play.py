import urllib2,json,datetime
from dateutil.parser import parse
from dateutil.tz import tzoffset
#date_format = '%Y-%m-%dT%H:%M:%S'

url = "https://graph.facebook.com/734097053/events?limit=10&access_token=CAACEdEose0cBAASQLM0ms35FvHucJXu0c6fiox9GsX1vmNJpsY9OBVlLUzHUTcTdpi8Yof6el4EMd92lHKqubjU3dQ9JXs6InWVkiDtPHXmsrNsRoqJW8iHL4adQ8nbIK9yR2iyOEfVVTHcX0exxx1kOZCvPeL9ZBA5vVDxItXfLKx1dCApnStbp8lBRhNJJ3gIpezITZB1Ohf1UzhEeFmHU75ttX8ZD"

token = "CAACEdEose0cBAASQLM0ms35FvHucJXu0c6fiox9GsX1vmNJpsY9OBVlLUzHUTcTdpi8Yof6el4EMd92lHKqubjU3dQ9JXs6InWVkiDtPHXmsrNsRoqJW8iHL4adQ8nbIK9yR2iyOEfVVTHcX0exxx1kOZCvPeL9ZBA5vVDxItXfLKx1dCApnStbp8lBRhNJJ3gIpezITZB1Ohf1UzhEeFmHU75ttX8ZD"

options = "limit=50"
user="me"
me_id = "10154596494280725"
method = "friends"
method = "events"

url = "https://graph.facebook.com/%s/%s?access_token=%s&%s" % (user,method,token,options)

response = urllib2.urlopen(url) ; data = json.loads(response.read().decode('utf-8'))

print len(data['data'])
for obj in data['data']:
    print obj['name']

while data['paging'].has_key('next'):
    for obj in data['data']:
        if obj.has_key("name"):
            event_date = parse(obj['start_time'])
            if event_date.year > 2009: #  > datetime.datetime(2010, 6, 1, 0, 0, tzinfo=tzoffset(None, -14400)):
                print obj['name']
    url = data['paging']['next']
    response = urllib2.urlopen(url)
    data = json.loads(response.read().decode('utf-8'))
    print len(data['data'])
