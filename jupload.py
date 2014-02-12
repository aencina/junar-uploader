from __future__ import with_statement
import sys
import urllib2
import csv
import settings 
import MultipartPostHandler

def UnicodeDictReader(utf8_data, **kwargs):
    csv_reader = csv.DictReader(utf8_data, **kwargs)
    for row in csv_reader:
        yield dict([(key, unicode(value, 'utf-8')) for key, value
                    in row.iteritems()])

def post_record(r):
    print "uploading %s"%r.get('title').encode('utf-8')
        
    form=dict(r)

    form['auth_key'] = settings.auth_key
    
    file_name = r.pop("file_data", None)
    
    if file_name is not None:        
        
        try:            
            file_data = open(file_name, 'rb')
            form['file_data'] = file_data    
          
            opener = urllib2.build_opener(MultipartPostHandler.MultipartPostHandler)
            response = opener.open(settings.url, form)
            
            print response.read()
        except Exception, e:
            print e    
        finally:
            file_data.close()
    else:
        try:                
            opener = urllib2.build_opener(MultipartPostHandler.MultipartPostHandler)
            response = opener.open(settings.url, form)
            
            print response.read()
        except Exception, e:
            print e          
        

if __name__=="__main__":  
    csv_name=sys.argv[1]
    
    csv_data = open(csv_name,"rb")
    try:
        for r in UnicodeDictReader(csv_data):
            post_record(r)
    finally:
        csv_data.close()
