__author__ = 'tibco'


fName = raw_input("Enter file name:")

fData = open(fName)

myList = list()
myUpList = list()
tempList = list()

for line in fData:
    line = line.rstrip()
    temp = line.split()
    myList.append(temp)
    temp = len(myList)
    print (len(myList))
i = 0
for i in range(temp):
    myUpList = myList[i] + myUpList

myUpList.sort()

for l in myUpList:
    if l not in tempList:
        tempList.append(l)

tempList.sort
print (tempList)
