# -*- coding: utf-8 -*-
"""
Created on Tue Nov 03 10:11:16 2015

@author: xiaoqin
"""

#import socket

#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('www.pythonlearn.com', 80))
#mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

#while True:
#    data = mysock.recv(512)
#    if ( len(data) < 1 ) :
#        break
#    print data;

#mysock.close()

import urllib
fhand = urllib.urlopen('http://www.maximuswang.com')
for line in fhand:
    print line.strip()