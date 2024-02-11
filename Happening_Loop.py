def happening(Num):
    if Num >= 1:
        for i in range (1, Num + 1):
            factorial = factorial * i
    return factorial
            
Num = int(input("Enter a number: "))
Answer = happening(Num)
print(Answer)
        