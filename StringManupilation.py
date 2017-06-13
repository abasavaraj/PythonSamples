__author__ = 'tibco'


# Use the file name mbox-short.txt as the file name


fName = raw_input("Enter file name: ")

try:
    fh = open(fName)
except:
    print("The File is not Valid")
    exit()
temp = []
count = 0
fValue = 0.0
for line in fh:

    line = line.rstrip()

    if line.startswith("X-DSPAM-Confidence:"):
        temp = float(line.strip("X-DSPAM-Confidence:"))
        count += 1
        fValue = fValue + temp

print "Average spam confidence:",fValue/count