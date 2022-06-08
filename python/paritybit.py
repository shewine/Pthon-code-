#sd means sender data
sd = input("\nEnter Data: ")

c = sd.count("1")
sd = sd + str(c%2)

print("\nParity Bit Appended: "+sd)

#For checking if dataframe is correct
#rd means reciver data
rd = input("\nEnter " +str(len(sd))+" Bits: ")

c = rd.count("1")

if(c%2 == 0):
	print("\nNo Error Found, code recieved correctly!\n")
else:
	print("\nError Found, code recieved incorrectly!\n")
