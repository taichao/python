
import sys,re,urllib

path = '/Users/zhangtaichao/Documents/ips/urls'
url = 'http://ips.chacuo.net/down/t_txt='


def getName(path):
    pattern = re.compile(r"href='http://ips.chacuo.net/view/(\w+)'")

    with open(path,'r') as f:
        res = pattern.findall(f.read())
        list = []
        for s in res:
            s = 'p' + s[1:]
            list.append(s)
        return list

if __name__ == '__main__':
    for i in getName(path):
        print('wget %s%s' % (url,i))

