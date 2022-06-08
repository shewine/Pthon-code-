from math import gcd as bltin_gcd



num = int(input("enter the prime no:"))
flag = False

# prime numbers are greater than 1
if num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

# check if flag is True
if flag:
    print(num, "is not a prime number")


else:
    print(num, "is a prime number")
    prime = num

    def primRoots(modulo):
        required_set = {num for num in range(1, modulo) if bltin_gcd(num, modulo) }
        return [g for g in range(1, modulo) if required_set == {pow(g, powers, modulo)
                for powers in range(1, modulo)}]

    print(primRoots(prime))

    
    g  = int (input("enter the value from above prime primitive no: "))
    a  = int (input("enter the a's secret key:"))
    b  = int (input("enter the b's secret key:"))


    A =(g**a) % prime
    print("public key of a to b: ",A)

    B =(g**b) % prime
    print("public key of b to a: ",B)

    sa = (B**a) % prime
    print("shared secret of a: ",sa)

    sb = (A**b) % prime
    print("shared secret of b: ",sb)
