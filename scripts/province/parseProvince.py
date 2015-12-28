# coding: utf-8
#读取execel使用(支持07)
from openpyxl import Workbook
#写入excel使用(支持07)
from openpyxl import load_workbook
import os

base = os.path.dirname(__file__)
pfile = os.path.join(base,'province.txt')


def parse(pfile) :
    with open(pfile,'r', encoding='utf-8') as f:
        for line in f.readlines():
            field = line.split();
            if len(field) < 3:
                continue
            print(field)

if '__main__' == __name__:
    parse(pfile)

