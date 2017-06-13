__author__ = 'tibco'

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
fData = dict()
lData = list()
for line in handle:
    line.rstrip()
    sLine = line.split()
    if "From" in sLine:
        dLine = sLine[5].split(":")
        fData[dLine[0]] = fData.get(dLine[0],0) + 1


for x in fData:
   lData.append(x)
lData.sort()

for z in lData:
    for x, y in fData.items():
        if z==x:
         print x,y