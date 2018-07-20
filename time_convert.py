# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time

#time stamp to time
ts = time.localtime(21489739212312)
print(time.strftime('%Y-%m-%dT%H:%M:%SZ', ts)) 

#time to time stamp
t = time.strptime('2012-10-21T18:51:50.000Z', '%Y-%m-%dT%H:%M:%S.%fZ')
print(time.mktime(t))