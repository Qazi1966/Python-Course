def happening(Num):
    mysum = 0
    for i in range(1, Num+1):
        mysum = mysum + i
    return mysum
    # if Num == 1:
    #     result = 1
    # else:
    #     result = happening(Num - 1) + Num
    # return result

Num = int(input("Enter a number: "))
Answer = happening(Num)
print(Answer)