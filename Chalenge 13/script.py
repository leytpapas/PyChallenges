#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import requests


#!/usr/bin/env python3
from urllib.request import urlopen
"""
try:
    with urlopen("http://www.pythonchallenge.com/pc/phonebook.php?f=remote") as response:
        print("Has content" if response.read(1) else "Content Empty")
        print(response.read().decode())
except OSError as e:
    print("error happened: {}".format(e))
"""
import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(s.system.listMethods())
calling = "Bert"
print("calling...", calling)
print(s.phone(calling)) # 555-ITALY
print("end of call")

# xml = "<?xml version='1.0' encoding='utf-8'?><call>evil</call>"
# headers = {'Content-Type': 'application/xml'} # set what your server accepts
# print (requests.post('http://www.pythonchallenge.com/pc/phonebook.php', data=xml.encode("utf-8"), headers=headers).text)
