find . -name "*."$1 |xargs wc -l|grep "total"|awk '{print $1}'
