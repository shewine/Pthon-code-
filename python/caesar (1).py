from secretpy import Ceaser


def encrypt():
    plaintext = input("Enter your Text:")
    key = int(input("Enter key value:"))
    cipher = Caesar()
    return(cipher.encrypt(plaintext, key))


def decrypt():
    plaintext = input("Enter your Text:")
    key = int(input("Enter key value:"))
    cipher = Caesar()
    return(cipher.decrypt(plaintext, key))


def main():
    choice = int(input("Enter your choice : \n 1.Encryption\n 2.Decrypt\n "))
    if(choice == 1):
        print(encrypt())
        main()
    elif(choice == 2):
        print(decrypt())
        main()

    else:
        print("Invalid Choice")


main()
