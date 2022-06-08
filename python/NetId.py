while(1):
    choice=input("\n1. Binary Form\n2. Dotted Decimal Form\nChoose the form of ip address:")
    mdata=input("\nEnter a Mask Number:")



    ip,bin,bytes,mask,nwadd=[0,0,0,0],"","","",[]
    def AND(ip,mask):
        for i in range(0,32,1):
            if ip[i]==mask[i]==1:
                nwadd.insert(i,"1")
            else:
                nwadd.insert(i,"0")
        return ''.join(nwadd)
    if mdata!="":
        for i in range(0,int(mdata),1):
            mask=mask+''.join("1")
        mask=mask+''.join((32-int(mdata))*"0")
    mask=[int(x) for x in mask]
    #print(mask)

    if choice=="1":
        ip=[int(x) for x in input("\nEnter an IP Address:")]
        nwadd = AND(ip, mask)
        print("\nNetwork Address: ",nwadd)
    elif choice=="2":
        bin=[int(x) for x in input("\nEnter an IP Address:").split(".")]
        print(bin)
        for i in range(0, 4, 1):
            if bin[i] == 128:
                ip[i] = ip[i] + 10000000
                bin[i] -= 128
            if bin[i] >= 64:
                ip[i] = ip[i] + 1000000
                bin[i] -= 64
            if bin[i] >= 32:
                ip[i] = ip[i] + 100000
                bin[i] -= 32
            if bin[i] >= 16:
                ip[i] = ip[i] + 10000
                bin[i] -= 16
            if bin[i] >= 8:
                ip[i] = ip[i] + 1000
                bin[i] -= 8
            if bin[i] >= 4:
                ip[i] = ip[i] + 100
                bin[i] -= 4
            if bin[i] >= 2:
                ip[i] = ip[i] + 10
                bin[i] -= 2
            if bin[i] == 1:
                ip[i] = ip[i] + 1
                bin[i] -= 1
            bytes=bytes+(8-len(str(ip[i])))*"0"+str(ip[i])
        print("\nBinary Form of IP address: ",bytes)
        ip=[int(x) for x in bytes]
        nwadd=AND(ip,mask)
        print("\nNetwork address: ",nwadd)
    else:
        print('enter valid choise id')
