#!/usr/bin/bash -l

# bash -l : use ~/.bash_profile
# MSERVER, WDIR, MY_MAIL_ADDR, etc

JSON=weather.json
PY=weather.py

if [ -f $JSON ]; then
	mv $JSON $JSON.old
fi

# 270000.json : Osaka Pref.
# $JSON get to ~/

wget --quiet -O - https://www.jma.go.jp/bosai/forecast/data/forecast/270000.json > ${JSON}

SUB=`date "+%B%d"`日の天気予報
python3 ${WDIR}/${PY} ${JSON}  | s-nail -A $MSERVER -s $SUB $MY_MAIL_ADDR
