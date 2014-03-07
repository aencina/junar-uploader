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
    print "uploading %s"%r.get('title').encode('utf-8')

    file_name = r.pop("file_data", None)
    form = dict(r)
    form['auth_key'] = settings.auth_key

    if file_name is not None:
        try:
            file_data = open(file_name, 'rb')
            print "Addind data [%s] file for %s" % (file_data.name, file_name)

            form['file_data'] = file_data
            # test form['is_file'] = "1"
            import pprint
            pp = pprint.PrettyPrinter(indent=4)
            print "SENDING ..."
            pp.pprint(form)

            opener = urllib2.build_opener(MultipartPostHandler())
            response = opener.open(settings.url, form)

            print response.read()
        except Exception, e:
            print e
        finally:
            file_data.close()
    else:
        try:
            print "file %s will be read from the web" % form["source"]
            opener = urllib2.build_opener(MultipartPostHandler())
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
