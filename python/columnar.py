from secretpy import ColumnarTransposition

def encrypt():
	plaintext = input("Enter your text:")
	key = input("Enter text-key:")
	cipher = ColumnarTransposition()
	print(cipher.encrypt(plaintext, key).upper())
def decrypt():
	plaintext = input("Enter your text:")
	key = input("Enter text-key:")
	cipher = ColumnarTransposition()
	print(cipher.decrypt(plaintext, key).upper())
def main():
	choice = int(input("Enter your choice : \n 1.Encryption\n 2.Decyption\n "))
	if(choice == 1):
		print(encrypt())
		main()
	elif(choice == 2):
		print(decrypt())
		main()
	else:
		print("Invalid Choice")
		
main()
