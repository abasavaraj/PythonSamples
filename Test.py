__author__ = 'tibco'

import urllib
import re

fhand = urllib.urlopen('http://www.py4inf.com/code/mbox-short.txt')


# fname = raw_input("Enter file name: ")
#if len(fname) < 1 : fname = "mbox-short.txt"
x = list()
#fData = open(fhand)
for line in fhand:
    y = re.findall('^From .*@([^ ]+)', line)
    if len(y) != 1: continue
    if y not in x:
        x.append(y)
print x




