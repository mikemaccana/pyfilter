#!/usr/bin/env python2.6
'''Client for pifilter image filtering service'''
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import urllib2
 
def checkimage(imagefilename,customerid,aggressive=True):
    '''Check an image for porn using PIFilter'''
    # Response Codes
    # http://pifilter.com/html/manual.html
    register_openers()
    responsecodes = {
        1:{
            'result':False,
            'reason':'Not porn',
            },
        2:{
            'result':True,
            'reason':'Porn',
            },
        3:{
            'result':aggressive,
            'reason':'Suspicious',
            },
        -10:{
            'result':None,
            'reason':'Billing Error: Query limit is over',
            },
        -11:{
            'result':None,
            'reason':'Billing Error: Unknown Control String',
            },
        -12:{
            'result':None,
            'reason':'Billing Error: Incorrect IP address',
            },
        -13:{
            'result':None,
            'reason':'Billing Error: Bandwidth limit is exceeded',
            },
        -20:{
            'result':None,
            'reason':'Data error: Incorrect URL',
            },
        -30:{
            'result':None,
            'reason':'Data error: Image is corrupt',
            },
        -31:{
            'result':None,
            'reason':'Data error: Image too small',
            },
        -32:{
            'result':None,
            'reason':'Data error: Image too big',
            },
        -40:{
            'result':None,
            'reason':'Unknown error',
            },
    }    
    
    # headers contains the necessary Content-Type and Content-Length
    # datagen is a generator object that yields the encoded parameters
    datagen, headers = multipart_encode({
        'ImageFile': open(imagefilename),
    	'ControlStr':customerid,        
        })

    # Create the Request 
    request = urllib2.Request('http://service.pifilter.com/Image.ashx', datagen, headers)
    # Send the request and get response
    # Note sometimes pifilter response include the ',<reason>', sometimes not.
    responsecode = urllib2.urlopen(request).read().split(',')[0]
    response = responsecodes[int(responsecode)]
    return response

if __name__ == '__main__':
    # Register the streaming http handlers with urllib2
    response = checkimage('static/cache/1280053613136.jpg','get_your_own_customer_id')
    print response