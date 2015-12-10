# coding: utf-8
import urllib.request
import urllib.parse
import params,json,time,runpy,filedata,dbservice
__author__ = 'zhangtaichao'

def post_event_api():
    host = params.host
    for event in params.event_list:
        url = host + params.apis['event']
        common_param            = params.common_param()
        func = event + "_param"
        res = runpy.run_module('params',run_name=func )
        event_param = res[func]()
        data = json.dumps(event_param)
        data = data.replace(' ','')
        common_param['data'] = data
        param = urllib.parse.urlencode(common_param,encoding='utf-8')
        print(param)
        param                   = param.encode('utf-8')
        req                     = urllib.request.Request(url=url,method='POST',data=param)
        req.add_header('X-Forword-For','1.1.1.1')
        print(url)
        with urllib.request.urlopen(req) as f:
            print(f.status)

def post_data_api():
    url                                       = params.host + params.apis['data']
    common_param                              = params.common_param()
    data_param                                = params.api_data_param()
    data                                      = json.dumps(data_param)
    data                                      = data.replace(' ','')
    common_param['data']                      = data
    param                                     = urllib.parse.urlencode(common_param,encoding='utf-8')
    print(param)
    param                                     = param.encode('utf-8')
    req                                       = urllib.request.Request(url=url,method='POST',data=param)
    req.add_header('X-Forword-For','1.1.1.1')
    print(url)
    with urllib.request.urlopen(req) as f:
        print(f.status)

def post_page_stay_api(data = None):
    common_param            = params.common_param()
    page_stay_param         = params.page_stay_param()
    param                   = urllib.parse.urlencode(common_param)
    param                   = "%s&data=%s" % (param,json.dumps(page_stay_param))
    url                     = params.host + params.apis['event']
    param                   = param.encode('utf-8')
    req                     = urllib.request.Request(url=url,method='POST',data=param)
    req.add_header('X-Forword-For','1.1.1.1')
    print(url)
    with urllib.request.urlopen(req) as f:
        print(f.status)


if __name__ == '__main__':
    while True:
        post_event_api()
        post_data_api()
        time.sleep(20)
