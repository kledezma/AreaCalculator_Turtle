userSelection = 0

while userSelection < 5:
    print("===================================")
    print("Area Calculator")
    print("1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Quit")
    print("===================================")

    userSelection = int(input("Select an option"))
    area = 0
    if userSelection == 1:
        height = int(input("what is the size of the heigth"))
        base = int(input("what is the size of the base"))
        area = (height*base)/2
        print("The Triangle area  is ",area)
    elif userSelection == 2:
        length = int(input("Insert the length"))
        width = int(input("Insert the the width"))
        area = length*width
        print("The Rectangle area is ",area)
    elif userSelection == 3:
        side = int(input("Insert size of the side"))
        area = side**2
        print("The Square area is ",area)
    elif userSelection == 4:
        radius = int(input("Insert the radius"))
        area = 3.14*(radius**2)
        print("The Circle area is ",area)

    elif userSelection == 5:
        print("You have exit")
    else:
        print("Invalid Selection")

  
