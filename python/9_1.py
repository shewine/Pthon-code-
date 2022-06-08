fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short"
count = dict()
maxcount=0
maxword=0
fh = open(fname)

#creating loop that read through each each line in a word file
for line in fh:
    # checking if the line starts with "From " if true then continue
    if not line.startswith("From ") is True : continue
    #splitting the line that start with "From "
    words=line.split()
    #saving email of sender in email and discarding all the other data
    email=words[1]
    #saving the email and their count in a dictionary
    count[email] = count.get(email,0)+1

for key,value in count.items():
    if maxcount is None or value > maxcount:
        maxword=key
        maxcount=value

print(maxword , maxcount)
