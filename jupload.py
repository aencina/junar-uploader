from __future__ import with_statement
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
    
    file_data = open(file_name, 'rb')
    try:
        
        form['file_data'] = file_data
      
        opener = urllib2.build_opener(MultipartPostHandler())
        response = opener.open(settings.url, form)
        
        print response.read()
    
    finally:
        file_data.close()

if __name__=="__main__":  
    csv_name=sys.argv[1]
    
    csv_data = open(csv_name,"rb")
    try:
        for r in UnicodeDictReader(csv_data):
            post_record(r)
    finally:
        csv_data.close()
