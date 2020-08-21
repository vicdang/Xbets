#!/bin/bash

function pre_start() {
   echo `/bin/date +'%Y-%m-%d %H:%M:%S %Z'`: START >> /var/log/xbets/xbets.log ||\
   true
   # TODO: Sanity checks

}

function start() {
   echo $$ > /var/run/xbets/pids/xbets.pid
   exec /home/ubuntu/Xbets/txbets/runserver manage.py runserver 0.0.0.0:80  >> /var/log/xbets/xbets.log 2>&1
}

function post_stop() {
   echo `/bin/date +'%Y-%m-%d %H:%M:%S %Z'`: STOP >> /var/log/xbets/xbets.log ||\
   true

   if test `find /var/run/xbets/pids/xbets.pid -mmin -0.1`; then
      rm -f /var/run/xbets/pids/xbets.pid
      exec sleep 5
   else
      rm -f /var/run/xbets/pids/xbets.pid
   fi
}

function invalid_action() {
   echo "$0: usage: {pre-start|start|post-stop}"
   exit 1
}

if [ "$#" -ne 1 ]
then
   invalid_action
fi

case "$1" in
   pre-start)
      pre_start
      ;;
   start)
      start
      ;;
   post-stop)
      post_stop
      ;;
   *)
      invalid_action
      ;;
esac
