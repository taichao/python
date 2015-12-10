#/bin/bash
#load mob_user to hive
#by ztc
path="/home/testdata/xhsdata_simulate/"
hour=`date +%H`
day=`date +%Y-%m-%d`
if [ "$hour" = "0" ];then
    hour="23"
    day=`date -d "-1 day" "+%Y-%m-%d"`

fi

file="$day""_""$hour"".txt"
file="$path""$file"
echo $file
