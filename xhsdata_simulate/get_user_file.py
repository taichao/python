# coding: utf-8
import dbservice,time,os,datetime

dstpath = os.path.join( os.path.dirname(__file__),'data' )

def write_user_file(day,hour,data):
    file = "user_{}{:02}.txt".format(day,hour)
    file = os.path.join(dstpath,file)
    with open(file,'w',encoding='utf-8') as f:
        for i in data:
            line = ''
            for j in i:
                if j:
                    line = line + j + chr(1)
                else:
                    line = line + 'null' + chr(1)
            f.write(line)
            f.write(os.linesep)


if __name__ == '__main__':
    db = dbservice.DBService()
    today = datetime.datetime.today()
    fmt = "%Y%m%d"
    hour = today.hour
    if hour == 0:
        hour = 23
        delta = datetime.timedelta(days=1)
        today = today - delta
    else:
        hour = hour - 1
    day = time.strftime(fmt,today.timetuple())
    res = db.get_user_forfile(day,hour)
    write_user_file(day,hour,res)
