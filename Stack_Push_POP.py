def Push(DataToPush):
    global StackData
    global StackPointer
    if StackPointer == 10:
        return False
    else:
        StackData[StackPointer] = DataToPush
        StackPointer = StackPointer + 1
        return True 

def Pop():
    global StackData
    global StackPointer
    if StackPointer == 0:
        return -1
    else:
        ReturnData = StackData[StackPointer - 1]
        StackData[StackPointer - 1] = 0
        StackPointer = StackPointer - 1
        return ReturnData

def PrintArray():
    global StackData
    global StackPointer
    print("Total Items in Stack  ", StackPointer)
    for x in range (0, 10):
        print(StackData[x])


StackPointer = 0
StackData = [0,0,0,0,0,0,0,0,0,0]


for x in range(0, 11):
    TempNumber = int(input("Enter a number"))
    
    if Push(TempNumber) == True:
        print("Stored")
    else:
        print("Stack full")
PrintArray()
print("Items removed ", Pop())
print("Items removed ", Pop())
print("Items removed ", Pop())
print("Items removed ", Pop())
print("Items removed ", Pop())
print("Items removed ", Pop())
print("Items removed ", Pop())
print("Items removed ", Pop())
print("Items removed ", Pop())
print("Items removed ", Pop())
print("Items removed ", Pop())
PrintArray()
