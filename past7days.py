import urllib2
import json

def past7days():
    url = "http://wichita.ogs.ou.edu/eq/catalog/past7days/past7days.json"
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    f = open('past7days.js', 'w')
    f.write('past7days = ')
    json.dump(data, f)
    
def past30days():
    url = "http://wichita.ogs.ou.edu/eq/catalog/past30days/past30days.json"
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    f = open('past30days.js', 'w')
    f.write('past30days = ')
    json.dump(data, f)   

def gatherdata():
    past7days()
    past30days()
    
gatherdata()