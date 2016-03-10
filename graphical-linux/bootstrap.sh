#!/usr/bin/env bash

wget -P /tmp  http://static.florian-berger.de/simplegui-0.1.0.zip
yum -y install zip unzip tkinter
unzip -u /tmp/simplegui-0.1.0.zip  -d /tmp
cd /tmp/simplegui-0.1.0;python setup.py install
#apt-get update
#apt-get install -y apache2
#if ! [ -L /var/www ]; then
#  rm -rf /var/www
#  ln -fs /vagrant /var/www
#fi
