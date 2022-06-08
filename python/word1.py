import re
from collections import Counter

s = input("Enter filename : ")
f = open(s, 'r')
text = f.read()

symbols = ['!', '@', '#', '$', '&', '^']
oparators = ['+', '-', '*', '/', '%', '=',
             '+=', '-=', '==', '<', '>', '<=', '>=']
keywords = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int',
            'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile', 'while']
delimiters = [' ', '   ', '.', ',', '\n', ';',
              '(', ')', '<', '>', '{', '}', '[', ']']


in_keywords = []
in_spl_symbols = []
in_oparators = []
in_delimiters = []
in_identifiers = []
in_constants = []

tokens = []
isStr = False
isWord = False
isCmt = 0
token = ''

for i in text:
    if i == '/':
        isCmt = isCmt+1

    elif isCmt == 2:
        if i == '\n':
            token = ''
            isCmt = 0

    elif i == '"' or i == "'":
        if isStr:
            tokens.append(token)
            token = ''
        isStr = not isStr

    elif isStr:
        token = token+i

    elif i in symbols:
        tokens.append(i)

    elif i.isalnum() and not isWord:
        isWord = True
        token = i

    elif (i in delimiters) or (i in oparators):
        if token:
            tokens.append(token)
            token = ''

        if not (i == ' ' or i == '\n' or i == '	'):
            tokens.append(i)

    elif isWord:
        token = token+i


for token in tokens:
    if token in symbols:
        in_spl_symbols.append(token)

    elif token in oparators:
        in_oparators.append(token)

    elif token in keywords:
        in_keywords.append(token)

    elif re.search("^[_a-zA-Z][_a-zA-Z0-9]*$", token):
        in_identifiers.append(token)

    elif token in delimiters:
        in_delimiters.append(token)

    else:
        in_constants.append(token)


print("No of tokens = ", len(tokens))
print("\nNo. of keywords = ", len(in_keywords))
pair_keywords = dict(Counter(in_keywords))
# print(pair_keywords);
print('Index  Count')
for index, count in pair_keywords.items():
    print(f'{index}\t{count}')
print("\nNo. of special symbols = ", len(in_spl_symbols))
pair_symbols = dict(Counter(in_spl_symbols))
# print(pair_symbols);
print('Index  Count')
for index, count in pair_symbols.items():
    print(f'{index}\t{count}')
print("\nNo. of oparators = ", len(in_oparators))
pair_oparators = dict(Counter(in_oparators))
# print(pair_oparators);
print('Index  Count')
for index, count in pair_oparators.items():
    print(f'{index}\t{count}')
print("\nNo. of identifiers = ", len(in_identifiers))
pair_identifiers = dict(Counter(in_identifiers))
# print(pair_identifiers);
print('Index  Count')
for index, count in pair_identifiers.items():
    print(f'{index}\t{count}')
print("\nNo. of constants = ", len(in_constants))
pair_constants = dict(Counter(in_constants))
# print(pair_constants);
print('Index  Count')
for index, count in pair_constants.items():
    print(f'{index}\t{count}')
print("\nNo. of delimiters = ", len(in_delimiters))
pair_delimiters = dict(Counter(in_delimiters))
# print(pair_delimiters);
print('Index  Count')
for index, count in pair_delimiters.items():
    print(f'{index}\t{count}')
f.close()
