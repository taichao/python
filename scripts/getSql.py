# coding: utf-8
__author__ = 'zhangtaichao'
import os
sqlpath="/Users/zhangtaichao/tmp/20151208"
resultfile = os.path.join(sqlpath,"result.sql")

def get_files(sqlpath):
    l = os.listdir(sqlpath)
    for name in l:
        r = os.path.splitext(name)
        if r[1] == '.src':
            yield os.path.join(sqlpath,name)

def getSql(filepath):
    r = os.path.splitext(filepath)
    basename = os.path.basename(r[0])


    cmt = ''
    result = ''
    result += "CREATE TABLE IF NOT EXISTS %s (\n" % basename
    with open(filepath,'r',encoding='utf-8') as f:
        count = 0
        for line in f.readlines():
            count+=1
            field = line.split();
            if len(field) == 2:
                cmt = field[0]
                continue
            elif count == 2:
                continue
            type = 'type'
            if len(field) == 3:
                if field[1] == 'string':
                    type = 'varchar(10)'
                elif field[1] == 'bigint':
                    type = 'int(11)'
                result += "%s %s NULL COMMENT '%s',\n" % (field[0],type,field[2])
    result = result[0:-2] + ")\n"
    result+="ENGINE = InnoDB\nCOMMENT = '%s';\n\n\n" % cmt
    print(result)
    with open(resultfile,'a',encoding='utf-8') as w:
        w.write(result)


if __name__ == '__main__':
    for i in get_files(sqlpath):
        getSql(i)
