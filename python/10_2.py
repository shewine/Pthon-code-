name = input("Enter file:")
#if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
count = dict()
pieces = dict()

for line in fh:
    if not line.startswith("From ") is True: continue
    words = line.split()
    email=words[5]
    email=email.split(':')
    email=email[0]
    count[email] = count.get(email , 0)+1
    pieces=sorted([(v,k) for v,k in count.items()])

for i,j in pieces:
    print(i,j)
