fname = input("Enter file name: ")
fh = open(fname)
lst = list()
lst1 = list()
for line in fh:
    piece=line.rstrip()
    lst=piece.split()
    for i in lst:
        if i not in lst1:
            lst1.append(i)
lst1.sort()
print(lst1)
