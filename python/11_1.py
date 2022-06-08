import re


name = input ("Enter file name:")
fh = open(name)
sum=0
for line in fh:
    x=re.findall('[0-9]+',line) #finding numbers with 0-9 with one or more digits like [4,45,786,9009] from a single line
    for i in x:
        y = int(i)
        sum = sum+y
print(sum)
