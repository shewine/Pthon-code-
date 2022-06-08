# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
t=0
c=0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    c=c+1
    f=line.find('0')
    z=float(line[f:])
    t +=z

a=t/c
print("Average spam confidence:",a)
