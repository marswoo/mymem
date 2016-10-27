#! /bin/sh

export LD_LIBRARY_PATH="./:./lib:/lib:/lib64:/usr/lib:/usr/lib64:/usr/local/lib:/usr/local/lib64"

mysqld &> /dev/null &

python ./web_main.py $1
