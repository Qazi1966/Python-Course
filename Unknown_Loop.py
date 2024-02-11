def IterativeUnknown(X, Y):
    Total = 1
    while X != Y:
         if X < Y:
            print(str(X + Y))
            X = X + 1
            Total = Total * 2
    else:
        X = X - 1
        Total = int(Total / 2)
    return Total
        
# MAIN PROGRAM
for i in range(3):
    X = int(input("Enter the value of X: "))
    Y = int(input("Enter the value of Y: "))
    result = IterativeUnknown(X, Y)
    print(result)
    print()