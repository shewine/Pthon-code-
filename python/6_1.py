
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try:
        number =int (num)
        if largest== None:
                largest=number
        elif largest < number :
                largest = number
        if smallest == None:
                smallest = number
        elif smallest > number:
                smallest = number

    except:
        print("Invalid input")
        continue






print("Maximum is", largest)
print('Minimum is', smallest)
