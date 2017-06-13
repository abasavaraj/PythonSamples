__author__ = 'tibco'

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
DataDist = dict()


for line in handle:
    line.rstrip()
    Data = line.split()
    if "From" in Data:
        DataDist[Data[1]] = DataDist.get(Data[1],0) +1
bigValue = 0
bigKey = 0

t = sorted(((j,i) for i,j in DataDist.items()),None,None,reverse=True)

print(t)

for k,v in DataDist.items():
    if v > 0 and v > bigValue:
        bigValue = v
        bigKey = k


print bigKey,bigValue