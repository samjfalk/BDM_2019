import sys
import json
import datetime
#import request
import urllib2

if __name__=='__main__':
    dataid = sys.argv[1]
    dataurl = 'http://nycopendata.socrata.com/views/%s' % dataid
    request = urllib2.urlopen(dataurl)
    metadata = json.loads(request.read())
    print(datetime.datetime.fromtimestamp(metadata['createdAt']))
