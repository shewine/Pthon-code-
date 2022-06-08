from secretpy import Caesar

def encrypt():
	plaintext = input("Enter your msg:")
	key = int(input("Enter your key:"))
	cipher = Caesar()
	return(cipher.encrypt(plaintext, key))
def decrypt():
	plaintext = input("Enter your msg:")
	key = int(input("Enter your key:"))
	cipher = Caesar()
	return(cipher.decrypt(plaintext, key))
def main():
	choice = int(input("Enter your choice : \n 1.Encryption\n 2.Decyption\n 3.Exit\n '='"))
	if(choice == 1):
		print(encrypt())
		main()
	elif(choice == 2):
		print(decrypt())
		main()
	elif(choice == 3):
		print("Arigato")
		exit()
	else:
		print("Bad Choice")

main()
