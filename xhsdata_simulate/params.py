# coding: utf-8
import uuid, random, time, urllib, filedata,dbservice

__author__ = 'zhangtaichao'

host = "http://123.56.143.227:4180"
apis = {
    'data': '/api/data/index',
    'device': '/api/device/index',
    'error': '/api/error/index',
    'event': '/api/event/index'
}
event_list = ["ad_show", "ad_click", "page_stay", "share", "comment", "collection" , "use_time"]
client_type_list = ["A", "I"]
app_version_list = ["1.0", "2.0", "3.0"]
channel_list = ["安智", "豌豆荚", "百度", "应用吧", "91助手"]
from_path_list = ["MainApplication", "searchApplication", "detailApplication", "listApplication"]

base_url_list = [
    "base_url_test1",
    "base_url_test2",
    "base_url_test3",
    "base_url_test4",
]
page_from_list = ["search","index","menu"]
page_from_id_list = [ "1","2","3" ]

page_type_list = ["index","search","news"]


device_name_list = [
    "Nubia",
    "Samsunc",
    "Nokia",
    "xiaomi",
    "Iphone",
    "Ipad"
]

def common_param(client_id,user_id):
    cp = {
        "appkey"      : "be631299c0fd9f16cf4e789d72630caa",
        "client_id"   : client_id,
        "clinetType"  : client_type_list[random.randint(0, 1)],
        "user_id"     : user_id,
        "app_version" : app_version_list[random.randint(0, len(app_version_list) -1)],
        "channel_id"  : channel_list[random.randint(0, len(channel_list) -1)],
        "from_path"   : from_path_list[random.randint(0, len(from_path_list) -1)],
        "imei"        : client_id,
        "mac"         : client_id,
        "idfa"        : client_id,
        "open_udid"   : client_id,
    }
    return cp


def api_data_param():
    row = dbservice.DBService().get_area()
    row = row[0]
    if row is not None:
        ip,country,province,city,area = row
    resolution_list = ["640x960", "100x100", "1024x680","1920x1000"]
    platform_list = ["android","ios"]
    os_list = ["ios","android","minui","huaweios",'3xos']
    os_version_list = ["1.0","2.1","3.1"]
    cp = {
        "device_name"  : device_name_list[random.randint(0,len(device_name_list) -1)],
        "have_bt"      : str(random.randint(0,1)),
        "have_gps"     : str(random.randint(0,1)),
        "java_support" : str(random.randint(0,1)),
        "have_gravity" : str(random.randint(0,1)),
        "resolution"   : resolution_list[random.randint(0,len(resolution_list) -1)],
        "platform"     : platform_list[random.randint(0,1)],
        "os"           : os_list[random.randint(0,len(os_list) -1)],
        "os_version"   : os_version_list[random.randint(0,len(os_version_list) -1)],
        "language"     : "zh",
        "wifimac"      : "d8-55-a3-ed-24-cb",
        "country":country,
        "province": province,
        "city":city,
        "address":area
    }
    return cp

def api_error_param():
    timen = int ( time.time() * 1000 )
    error_list = ["Null","e","e1","e22","e333","e444"]
    cp = {
        "time":timen,
        "stacktrace":error_list[random.randint(0,len(error_list) -1)]
    }
    return cp

def page_stay_param():
    out_time = int(time.time() * 1000)
    stay_time = random.randint(1,1000)
    in_time = out_time - stay_time

    param = {
        "aname":"page_stay",
        "base_url"     : base_url_list[random.randint(0,len(base_url_list) -1 )],
        "page_from"    : page_from_list[random.randint( 0,len(page_from_list) -1)],
        "page_from_id" : page_from_id_list[random.randint(0,len(page_from_id_list) -1)],
        "page_type"    : page_type_list[random.randint(0,len(page_type_list) -1)],
        "page_key"     : filedata.get_news_id().__next__(),
        "in_time"     : str(in_time),
        "out_time"     : str(out_time),
        "stay_time"    : str(stay_time),
        "read_status"  : str(random.randint(1,100))
    }

    return param

def ad_show_param():
    ad_id = filedata.get_ad_id().__next__()
    seq_id = random.randint(1,10)
    pos_list = ["index","news","list"]
    ad_pos = pos_list[random.randint(0,len(pos_list) -1)]
    param = {
        "aname":"ad_show",
        "ad_id"  : ad_id,
        "seq_id" : seq_id,
        "ad_pos" : ad_pos
    }
    return param

def ad_click_param():
    ad_id = filedata.get_ad_id().__next__()
    seq_id = random.randint(1,10)
    pos_list = ["index","news","list"]
    ad_pos = pos_list[random.randint(0,len(pos_list) -1)]
    param = {
        "aname":"ad_click",
        "ad_id"  : ad_id,
        "seq_id" : seq_id,
        "ad_pos" : ad_pos
    }
    return param
def share_param():
    share_to_list = ["qq","weixin","weibo","qzone"];
    param = {
        "aname":"share",
        "base_url"     : base_url_list[random.randint(0,len(base_url_list) -1 )],
        "page_type"    : page_type_list[random.randint(0,len(page_type_list) -1)],
        "page_key"     : filedata.get_news_id().__next__(),
        "share_to"  : share_to_list[random.randint(0,len(share_to_list) -1)]
    }
    return param

def comment_param():
    param = {
        "aname":"comment",
        "base_url"     : base_url_list[random.randint(0,len(base_url_list) -1 )],
        "article_menu" : filedata.get_category_id().__next__(),
        "article_key": filedata.get_news_id().__next__()
    }
    return param

def collection_param():
    param = {
        "aname":"collection",
        "base_url"     : base_url_list[random.randint(0,len(base_url_list) -1 )],
        "article_menu" : filedata.get_category_id().__next__(),
        "article_key": filedata.get_news_id().__next__()
    }
    return param


def use_time_param():
    out_time = int(time.time() * 1000)
    stay_time = random.randint(1,1000)
    in_time = out_time - stay_time
    param = {
        "aname":"use_time",
        "in_time"     : str(in_time),
        "out_time"     : str(out_time),
        "stay_time"    : str(stay_time),
    }
    return param
