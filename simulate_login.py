# -*- coding:utf-8 -*-
import urllib2
import urllib

if __name__ == "__main__":
    data = {}
    data['LoginName'] = '19881917'
    data['Password'] =  '18a87db830e9d59a5ab99e730bf55aed3562771a80ad078b89ba0a12fb08f8467724a812bccc35d2766f82d143a44aef3a7e7d1ce5f24758349b745656c25538'
    data['UniversityCode'] = '10338'
    data['LoginWay'] = 'Number'
    print data
    #
    # user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36'}
    url = 'http://59.77.139.103/index.html'
    post_data = urllib.urlencode(data)

    request = urllib2.Request(url, headers=headers)
    #
    req = urllib2.urlopen(post_data,request)

    #
    content = req.read()

    print
    print content