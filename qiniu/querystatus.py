# coding: utf-8
__author__ = 'zhangtaichao'

import urllib.request

qiniuhost = 'http://api.qiniu.com'

prefop = qiniuhost + '/status/get/prefop?id='


id = 'z0.568243aa7823de14f711d6d9'
with urllib.request.urlopen(prefop + id) as f:
    res = f.read()
    print(res.decode('utf-8'))

#  mghqkWoETCwselwlNCjwMZAmniY=/lsriD3gagsfYXKjxzUuLBe8LVQSl