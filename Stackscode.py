def push (num, stack):
    global headpointer
    if (headpointer < maxstacksize - 1):
        headpointer = headpointer + 1
        stack[headpointer] = num
    else:
        print("Stack is empty, Cannot POP")
def pop(stack):
    global headpointer
    print(stack[headpointer])
    headpointer = headpointer - 1

emptystring = ""
nullpointer = -1
maxstacksize = 20
basepointer = 0
headpointer = nullpointer
stack = []
while True:
    print("What do you want to do? ")
    print("1. Push")
    print("2. Pop")
    print("3. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        if(len(stack) == maxstacksize):
            print("Stack is full.")
        else:
            value = input("Enter the value: ")
            stack.append(value)

        print('Stack after elements are pushed:', stack)

    elif choice == 2:
        if(len(stack) == 0):
            print("Stack is empty.")
        else:
            stack.pop()

        print('Stack after elements are popped:', stack)
    elif choice == 3:
        break

    else:
        print("Invalid choice.")
    print()