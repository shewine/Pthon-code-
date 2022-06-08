choice=input("\n1. Binary Form\n2. Dotted Decimal Form\nChoose the form of ip address:")
ip,bin,bytes,mask,nwadd=[0,0,0,0],"","","",[]
def classes(bin):
    if bin in range(0, 128):
        print("\nIP address belongs to Class A")
    elif bin in range(128, 192):
        print("\nIP address belongs to Class B")
    elif bin in range(192, 224):
        print("\nIP address belongs to Class C")
    elif bin in range(224, 240):
        print("\nIP address belongs to Class D")
    elif bin in range(240, 256):
        print("\nIP address belongs to Class E")
    else:
        print("\nIP address is incorrect")
def check(ip):
    temp, c = 0, 7
    bin=""
    for i in range(0, 32, 1):
        if(ip[i] == 1 or ip[i] == 0):
            if (ip[i] == 1):
                temp = temp + 2 ** c
            c -= 1
        else:
            break
        if c == -1:
            c = 7
            bin = bin + str(temp)+"."
            temp=0
    bin = bin.split(".")
    classes(int(bin[0]))
if choice=="1":
    ip=[int(x) for x in input("\nEnter an IP Address:")]
    check(ip)
elif choice=="2":
    bin=[int(x) for x in input("\nEnter an IP Address:").split(".")]
    print(bin)
    classes(bin[0])
else:
    print("\nPlease enter correct option:)")
