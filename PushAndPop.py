#VARIABLES
maxStackSize = int(input("Enter stack size: "))
nullPointer = -1
baseStackPointer = 0
topStackPointer = nullPointer
stackArray = [""] * maxStackSize

#PROCEDURE FOR PUSHING AN ITEM AKA ADDING AN ITEM TO THE STACK ARRAY
def Push(newItem) :
    global topStackPointer
    if topStackPointer < maxStackSize - 1 :
        topStackPointer = topStackPointer + 1
        stackArray[topStackPointer] = newItem
    else :
        print("STACK FULL")
    print(stackArray)

#FUNCTION FOR POPPING AN ITEM AKA DELETING AN ITEM TO THE STACK ARRAY
def Pop() :
    global topStackPointer
    global item
    item = ""
    if topStackPointer > nullPointer :
        item = stackArray[topStackPointer]
        stackArray[topStackPointer] = ""
        topStackPointer = topStackPointer - 1
    print(stackArray)
    print("Number popped:" , item)
    return item

#CALLS
call = ""
while call != "QUIT" :
    call = input("Enter call (Type either PUSH or POP or QUIT): ")
    if call == "PUSH" :
        newPushItem = input("Enter new item to push: ")
        Push(newPushItem)
    elif call == "POP" :
        Pop()