__author__ = 'tibco'


fruit = "Banana"

for i in fruit:
    print("Success")

basket = "Mango" + " " + fruit
print basket
i = 0
j=" "
k = 0
numbers = []
while i < len(basket):
    print(basket[1:])
    if(j == basket[i]):
        print(i)
        k = i
        print(basket[k+1:])


    i=i+1

if "t" in fruit:
    print("Failure")
else:
    print("Success")

text = "X-DSPAM-Confidence:    0.8475";
data = text.find("0")

print(text[data:])

temp = open("http://www.pythonlearn.com/code/words.txt")

tread = temp.read()
print tread
print len(tread)

#temp.close()
try:
    temp = open("Test.txt")

except:
    print("The File does not exist",temp)
    exit()

count = 0
for line in temp:
    line = line.rstrip()
    if not line.startswith('TEST::'):
        continue

    print(line)
    count += 1

print(count)

