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
    print "uploading %s" % r.get('title').encode('utf-8')

    form = dict(r)
    form['auth_key'] = settings.auth_key

    try:

        import pprint
        pp = pprint.PrettyPrinter(indent=4)
        print "SENDING TO %s ..." % settings.url_webservice
        pp.pprint(form)

        opener = urllib2.build_opener(MultipartPostHandler())
        response = opener.open(settings.url_webservice, form)

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
"""

CSV sample

title,description,category,tags,endpoint,impl_type,path_to_data,path_to_headers,token,algorithm,signature,username,password
Webservice Test01 title,Webservice description text,Test,"tag01, tag02",http://api_enpoint.com,14,data,header,token,sign_algoritm,sign_name,user,pass

impl_type = 14 => REST/JSON
impl_type = 1  => SOAP/XML

"""
