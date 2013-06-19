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
    form['file_data'] = open(file_name, 'rb')
  
    opener = urllib2.build_opener(MultipartPostHandler())
    opener.open(settings.url, form)   


if __name__=="__main__":  
    csvsource=sys.argv[1]
    for r in UnicodeDictReader(open(csvsource,"rb")):
        post_record(r)
