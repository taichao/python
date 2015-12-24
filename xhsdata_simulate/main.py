# coding: utf-8
import urllib.request
import urllib.parse
import params,json,time,runpy,filedata,dbservice,random
import datetime
__author__ = 'zhangtaichao'

def post_event_api(client_id,user_id = None):
    host = params.host
    for event in params.event_list:
        if event == 'ad_click':
            if random.randint(1,100) < 90:
                print('ad_click pass')
                continue
        url          = host + params.apis['event']
        common_param = params.common_param(client_id,user_id)
        func         = event + "_param"
        res          = runpy.run_module('params',run_name=func )
        event_param  = res[func]()
        send(url,common_param,event_param)
def send(url,common_param,data_param):
    data                 = json.dumps(data_param,ensure_ascii=False)
    data                 = data.replace(' ','')
    common_param['data'] = data
    param                = urllib.parse.urlencode(common_param,encoding='utf-8',safe=":")
    #logit = "[{}]-[{}]".format(url,param)
    #print(logit)
    param                = param.encode('utf-8')
    req                  = urllib.request.Request(url=url,method='POST',data=param)
    req.add_header('X-Forword-For','1.1.1.1')
    with urllib.request.urlopen(req) as f:
        if f.status != 204:
            print(f.status)


def post_data_api(client_id,user_id = None):
    url          = params.host + params.apis['data']
    common_param = params.common_param(client_id,user_id)
    data_param   = params.api_data_param()
    send(url,common_param,data_param)

def post_error_api(client_id,user_id = None):
    url          = params.host + params.apis['error']
    common_param = params.common_param(client_id,user_id)
    data_param   = params.api_error_param()
    send(url,common_param,data_param)


if __name__ == '__main__':
    while True:
        try:
            print(datetime.datetime.today())
            if random.randint(0,10) > 8:
                dbservice.DBService().create_client_id()
            info = dbservice.DBService().get_client_info()
            print(info)
            client_id = info[0]
            user_id = info[1]
            if user_id is None:
                ran = random.randint(1,100)
                if ran > 90:
                    ds = dbservice.DBService()
                    ds.create_user(client_id)
                    user_id = ds.get_user()[0]
                else:
                    user_id = ''
            post_data_api(client_id,user_id)
            if random.randint(1,100) > 90:
                print('send a error')
                post_error_api(client_id,user_id)
            post_event_api(client_id,user_id)
            time.sleep(1)
        except Exception as e:
            print(str(e))
