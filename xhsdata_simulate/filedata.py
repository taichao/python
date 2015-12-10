# coding: utf-8
__author__ = 'zhangtaichao'

import fileinput, random, uuid, time, linecache

files = ('data/news.txt','category.txt')
user_file = 'data/user.txt'
def get_news_id():
    list = []
    for line in fileinput.input(files=('data/news.txt')):
        list.append(line.strip())
    yield list[random.randint(0,len(list) -1)]

def get_category_id():
    list = []
    for line in fileinput.input(files=('data/category.txt')):
        list.append(line.strip())
    yield list[random.randint(0,len(list) -1)]

def get_ad_id():
    list = []
    for line in fileinput.input(files=('data/ad.txt')):
        list.append(line.strip())
    yield list[random.randint(0,len(list) -1)]

def create_user():
    user_id = int(time.time())
    client_id = uuid.uuid1()
    with open(user_file,'a') as f:
        f.write(str(user_id) + "," + str( client_id ) + "\n")
def get_user():
    count = 0
    for i,line in enumerate(open(user_file)):
        count = i
        pass
    num = random.randint(1,count -1 )
    line = linecache.getline(user_file,num)
    linecache.checkcache(user_file)
    print("count:%s  num:%s" % (count,num))
    field = line.split(',')
    if len(field) == 2:
        return (field[0].strip(),field[1].strip())
    else:
        print(line)
