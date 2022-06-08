from secretpy import Playfair

def encrypt():
	plaintext = input("Enter your msg:")
	key = input("Enter your key-text:")
	cipher = Playfair()
	print(cipher.encrypt(plaintext, key).upper())
def decrypt():
	plaintext = input("Enter your msg:")
	key = input("Enter your key-text:")
	cipher = Playfair()
	print(cipher.decrypt(plaintext, key).upper())
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
		print("Bad choice")

main()
