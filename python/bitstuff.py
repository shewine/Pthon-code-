


fr = input("\nEnter Data: ")


print("\nBefore Stuffing: "+fr+"\n")

for i in range(0,len(fr)):
	if(fr[i:i+6]=="011111"):
		fr = fr[:i+6]+"0"+fr[i+6:]



flag = " 01111110 "


print("\nBitstuffed Frame: "+flag+fr+flag)



for i in range(0,len(fr)):
	if(fr[i:i+6]=="011111"):
		fr = fr[:i+6]+fr[i+7:]


print("\nRecovered Frame: "+fr+"\n")
