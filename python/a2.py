print("what do u want to convert")
# taking ip about what type of conversion they want
conversion = input(
    "(W)eight or (H)eight or (A)rea or (V)volume or (T)temperature :  ")
if conversion.upper() == "W":  # user choose "W" for weight

    weight = input("enter your weight :   ")
    print("enter the  unit of weight u are entering")
    unit = input('(L)bs or (K)gs or (O)z : ')
    print("enter the  unit of weight u are want")
    unit_want = input('(L)bs or (K)gs or (O)z : ')
    if unit.upper() == "K":
        if unit_want.upper() == "L":
            W = float(weight) * 0.45
            print(f"your weight is {W} lbs")
        else:
            W = float(weight) * 0.028349
            print(f"your weight is {W} oz")

    if unit.upper() == "L":
        if unit_want.upper() == "K":
            W = float(weight) // 0.45
            print(f"your weight is {W} Kgs")
        else:
            W = float(weight) * 16
            print(f"your weight is {W} oz")

    if unit.upper() == "O":
        if unit_want.upper() == "L":
            W = float(weight) // 0.062499
            print(f"your weight is {W} lbs")
    else:
        W = float(weight) // 0.028349
        print(f"your weight is {W} Kgs")
    if conversion.upper() == "H":

        print("if statement is working")

    if conversion.upper() == "A":

        print("if statement is working")
    if conversion.upper() == "V":

        print("if statement is working")

    if conversion.upper() == "T":

        print("if statement is working")
