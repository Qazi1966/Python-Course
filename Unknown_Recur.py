def Unknown(X, Y):
    if X < Y:
        print(X + Y)
        return Unknown(X + 1, Y) * 2
    else:
        if X == Y:
            return 1
        else:
            print(str(X + Y))
            return int(Unknown(X - 1, Y) / 2)

# MAIN PROGRAM
for i in range(3):
    X = int(input("Enter the value of X: "))
    Y = int(input("Enter the value of Y: "))
    result = Unknown(X, Y)
    print(result)
    print()