#!/bin/bash

################################
####                        ####
####        同步文件        ####
####        zhangtaichao        ####
####        2015/12/09      ####
####                        ####
################################


path_local="/Users/zhangtaichao/code/python/xhsdata_simulate"
path_line="testdata@xhs227.aliyun.server.com:~/"
rsync $path_local -az --exclude-from=/Users/zhangtaichao/code/python/xhsdata_simulate/exclude.list $path_line
