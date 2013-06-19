import sys
import urllib2
import csv
import settings 
from MultipartPostHandler import * 

def UnicodeDictReader(utf8_data, **kwargs):
    csv_reader = csv.DictReader(utf8_data, **kwargs)
    for row in csv_reader:
        yield dict([(key, unicode(value, 'utf-8')) for key, value
                    in row.iteritems()])

def post_record(r):
    print "uploading %s"%r.get('title')
    
    file_name=r.pop("file_data")
    
    form=dict(r)
      
    form['auth_key'] = settings.auth_key
    
    with open(file_name, 'rb') as file_data:
        
        form['file_data'] = file_data
      
        opener = urllib2.build_opener(MultipartPostHandler())
        response = opener.open(settings.url, form)
        
        print response.read()

        

if __name__=="__main__":  
    csvsource=sys.argv[1]
    
    with open(csvsource,"rb") as csv:
        for r in UnicodeDictReader(csv):
            post_record(r)
