__author__ = 'tibco'

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fData = list()
fh = open(fname)

for line in fh:
    line = line.rstrip()
    temp = line.split()
    if temp == []: continue
    if temp[0] == "From":
        fData.append(temp[1])
for i in fData:
    print i

count = len(fData)
print "There were", count, "lines in the file with From as the first word"
