__author__ = 'tibco'


fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fData = list()
fTemp = list()
fData1 = list()
fh = open(fname)

for line in fh:
    line = line.rstrip()
    if line.startswith("From"):

        temp = line.split()
        fData.append(temp)

ranData = len(fData)
i = 0
for i in range(ranData):
    if "From:" not in fData[i]:
        fTemp = fData[i] + fTemp

for i in fTemp:
    if "@" in i:
        fData1.append(i)
fData1.reverse()
for i in fData1:
    print i

count = len(fData1)
print "There were", count, "lines in the file with From as the first word"

