# coding: utf-8
__author__ = 'zhangtaichao'

src = '/Users/zhangtaichao/code/python/scripts/gensql/sh_shop.src'

def gensql(plist):
    table = plist[0]
    s = 'CREATE TABLE IF NOT EXISTS {} (\n'.format(table[1])
    for l in plist[1:]:
        name = l[0]
        tp = l[1]
        if 'int' in tp:
            tp = 'int(11)'
        elif 'double' in tp:
            tp = 'double'

        comment = l[2]
        if '否' in l[3]:
            nn = 'NOT NULL'
        else:
            nn = 'NULL'
        tmp = '{} {} {} COMMENT  \'{}\''.format(name,tp,nn,comment)
        s = s + tmp
        if l == plist[len(plist)-1]:
            s = s + "\n)\n"
        else:
            s = s + ',\n'


    s = s + "ENGINE = InnoDB\n"
    s = s + "COMMENT '{}';\n".format(table[0])
    print(s)


with open(src,'r',encoding='utf-8') as f:
    l = []
    for line in f.readlines():
        if len(line.strip()) == 0:
            gensql(l)
            l = []
            continue

        fields = line.split()
        l.append(fields)

    gensql(l)

