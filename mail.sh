#!/bin/bash
account='1172789766@qq.com'
password='budxbjbzirekhegi'
subject=$1
content=$2
sendemail -f $account -t $account -s smtp.qq.com:587 -u $subject  -xu $account -xp $password -m $content
 