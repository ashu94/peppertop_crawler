 
import json
import urllib2
import csv

# open the url and the screen name 
# (The screen name is the screen name of the user for whom to return results for)
url = "https://api.peppertap.com/user/shop/14/products/?zone_id=10"

# this takes a python object and dumps it to a string which is a JSON
# representation of that object
data = json.load(urllib2.urlopen(url))

with open(""+'.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter='"',
                            quotechar=',', quoting=csv.QUOTE_MINIMAL)

    for i in data['pl']:
        name = str(i['tle'])
        typ = str(i['typ'][0])
    
        for j in i['ps']:
            uid = str(j['uid'])
            dft = j['dft']
            sp = str(j['sp'])
            mrp = str(j['mrp'])
            qnt = str(j['da'])
        
            print "\n"
            print "\n"
            row = [uid.encode('ascii','ignore')]+[name.encode('ascii','ignore')]+[typ.encode('ascii','ignore')]+[mrp.encode('ascii','ignore')]+[sp.encode('ascii','ignore')]+[qnt.encode('ascii','ignore')]
            #row1= [uid.encode('ascii','ignore')]
            #print uid                             
            spamwriter.writerow(row) 
    

