import nltk
from nltk.tokenize import word_tokenize

fname=input("Enter file name:")
file = open(fname)
result = file.read()

# divides sentence into individuial words
words = word_tokenize(result)

word = 0
digit = 0
Special = 0

text = []
for i in range(len(words)):
	print(words[i])
	text.insert(i,words[i])
print(text)

for i in range(len(text)):
	if(text[i].isalpha()):
		word = word + 1
	elif(text[i].isdigit()):
		digit = digit + 1
	else:
		Special = Special + 1
print("\n")
print("Count of Words:",word)
print("Count of Numbers:",digit)
print("Count of Special-Characters:",Special)
