#!/bin/bash

mysql='mysql -uroot -p123456 -h 192.168.0.1'
cur_date=$(date -d '-10 min' +%Y-%m-%d\ %H:%M)
sql="use w; update t set status='c' where status=\"o\" and created_time<'$cur_date'"
$mysql -e "$sql"
