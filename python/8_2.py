fname = input("Enter file name: ")
#if len(fname) < 1 : fname = "mbox-short.txt"
c=0
lst=list()
fh = open(fname)
for line in fh:
    if not line.startswith("From ") is True : continue
    words=line.split()
    #print(words)
    email=words[1]
    lst.append(email)
for i in lst:
    c=c+1
    print(i)
print("There were", c, "lines in the file with From as the first word")
