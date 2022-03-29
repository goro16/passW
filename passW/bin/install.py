#!/usr/bin/python3

import os

os.system('touch db.txt')
os.system('echo "url,   username,   password" >> db.txt ')
os.system('chown root db.txt')
os.system('chmod a-wrx db.txt')
os.system('chown root bin/password.py')
os.system('chmod a-wrx bin/password.py')
print("installation finish")
