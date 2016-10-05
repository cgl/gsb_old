import urllib.request ,json,datetime
from dateutil.parser import parse
from dateutil.tz import tzoffset
#date_format = '%Y-%m-%dT%H:%M:%S'

# https://developers.facebook.com/docs/graph-api/reference/event

# get token https://developers.facebook.com/tools/explorer

def form_url(limit=150,user="me",method = "events"):
    token = "CAACEdEose0cBAOjaPlK2J6eo0Jy1OYFBQb9ZBzbZBEuuZBeNVaNdIy4V7BFNe7aPYqM7pL4J2geoWifDtQF60CUqiSmIGJwGcqwCYlJOdUrhk4SZCY8obP4ZBGgZBMDcbl8wSKYPoQPcHeegvpCHJhJZAUCsZAlz2hkD0oh1CrnS7MjOCXOKrBhbB4RQv6HZBmysSeAoMHFkF6gZDZD"
    options = "limit=%d" %limit
    me_id = "10154596494280725"
    #method = "friends"

    url = "https://graph.facebook.com/%s/%s?access_token=%s&%s" % (user,method,token,options)
    return url

def get_data(url):
    response = urllib.request.urlopen(url) ; data = json.loads(response.read().decode('utf-8'))
    return data

def get_event_list(data,Verbose=False):
    events = []
    #print(len(data['data']))
    for obj in data['data']:
        event_date = parse(obj['start_time'])
        if Verbose:
            print("%d %d %s" %(event_date.year,event_date.month,obj['name']))
        events.append((obj['id'],obj['name']))
    return events

def get_event_details(event_id):
    url = form_url(limit=10,user=str(event_id),method = "")
    event = get_data(url)
    event_date = parse(event['start_time'])
    print("%d %d %s" %(event_date.year,event_date.month,event['name']))
    if "description" in event:
        print(event['description'])
    return event


def print_next_page(data):
    while "next" in data['paging']:
        for obj in data['data']:
            if "name" in obj:
                event_date = parse(obj['start_time'])
                if event_date.year > 2009: #  > datetime.datetime(2010, 6, 1, 0, 0, tzinfo=tzoffset(None, -14400)):
                    pass #print("%s\n%s\n%s" %(obj['name'],obj['description'],event_date))
        url = data['paging']['next']
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        print(len(data['data']))

if __name__=="__main__":
    url = form_url(limit=50)
    data = get_data(url)
    events =get_event_list(data,Verbose=False)
    """
    while "next" in data["paging"]:
        url = data["paging"]["next"]
        data = get_data(url)
        events =get_event_list(data)
    """
    event_details = [get_event_details(event_id) for event_id,name in events]
    #print(url)
