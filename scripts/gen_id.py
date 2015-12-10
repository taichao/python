# coding: utf-8

import sys,os,random,re,httplib,codecs
from ipip import IP

root = '/Users/zhangtaichao/Documents/ips'
datapaht = '/Users/zhangtaichao/code/php/duobaohui_php/app/libraries/class/ip/17monipdb.dat'
IP.load(os.path.abspath(datapaht))

def get_files(path):
    l = os.listdir(root)
    for name in l:
        if name.startswith('t_txt'):
            yield os.path.join(path,name)

def for_file(file,num,inc=1):
    """
    :param file: ip段文件
    :param num: 每行最大生成个数
    :return:list
    """
    dic = {}
    (filepath,filename)=os.path.split(file)
    dic["name"] = filename[-2:]
    result = []
    with open(file,'r') as f:
        for line in f.readlines():
            ips = line.split()
            if(len(ips) == 3):
                res = gen_ip(ips[0],ips[1],num,inc)
                if type(res) == list:
                    result[len(result):len(result)] = res
    dic["ip"] = result
    return dic


def gen_ip(start,end,num,inc=1):
    """
    :param start: 初始ip
    :param end: 结束ip
    :param num: 最大生成ip数量
    :param inc: 每个ip大小间隔
    :return: list
    """
    regexIP=re.compile('^([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])\.([01]?\d\d?|2[0-4]\d|25[0-5])$')
    if regexIP.match(start) is None or regexIP.match(end) is None:
        print("bad input ips start:%s  end:%s" % (start,end))
        return []
    sl = start.split('.')
    el = end.split('.')
    print("from %s to %s" % (sl,el))
    result = []
    b1 = int(sl[0])
    b2 = int(sl[1])
    b3 = int(sl[2])
    b4 = int(sl[3])

    e1 = int(el[0])
    e2 = int(el[1])
    e3 = int(el[2])
    e4 = int(el[3])
    t1 = b1
    while t1 <= e1:

        t2 = b2
        while t2 <= e2:
            t3 = b3
            while t3 <= e3:
                t4 = b4
                while t4 < e4:
                    ip = "%s.%s.%s.%s" % (t1,t2,t3,t4);
                    result.append("%s.%s.%s.%s" % (t1,t2,t3,t4))
                    if int(num) <= len(result):
                        return result
                    t4 += inc
                t3 += inc
            t2 += inc
        t1 += inc
    return result


def insert(dict_data):
    pass

def url2php(dict):
    httpClient = None
    name = dict['name']
    list = dict['ip']
    httpClient = httplib.HTTPConnection('local.duobaohuiphp.com')
    for ip in list:
        url = "/ip?ip=%s&name=%s" % (ip,name);
        httpClient.request('GET',url)
        res = httpClient.getresponse();
        print(res.read())
        # print(url)
    httpClient.close()

def write2file(path,data):
    name = data['name']
    list = data['ip']
    with codecs.open(path,'a','utf-8') as f:
        sql = 'insert into sh_ip_factory(ip,country,province,city,county,remark) values'
        f.write(sql)
        for ip in list:
            res = IP.find(ip)
            res = res.split();

            if res == 'N/A' or len(res) == 1:
                continue
            while len(res) < 4:
                res.append('');
            res = tuple(res)
            (country,province,city,county) = res
            data = " ('%s','%s','%s','%s','%s','%s')," % (ip,country,province,city,county,name)
            f.write(data)
            f.write(os.linesep)

sqlp = '/Users/zhangtaichao/Documents/ips/ip.sql'
if __name__ == '__main__':

    for i in get_files(root):
        res = for_file(i,1000,2)
        write2file(sqlp,res)

