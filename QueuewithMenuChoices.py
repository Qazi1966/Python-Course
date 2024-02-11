def Enqueue(Queue, Head, Tail, NumItems, InputData):
 if NumItems >= 10:
     return (False, Queue, Head, Tail, NumItems)
 Queue[Tail] = InputData
 if Tail >= 9:
     Tail = 0
 else:
     Tail = Tail + 1
 NumItems = NumItems + 1
 return (True, Queue, Head, Tail, NumItems) 


def Dequeue(Queue, Head, Tail, NumItems):
 if NumItems == 0:
     return (False, Queue, Head, Tail, NumItems)
 else:
     ReturnValue = Queue[Head]
     Head = Head + 1
     if Head >= 9:
         Head = 0
         NumItems = NumItems - 1
     return(ReturnValue, Queue, Head, Tail, NumItems)

QueueArray = [''] * 10  #string
QueueHeadPointer = 0    #integer
QueueTailPointer = 0    #integer
NumberOfItems = 0       #integer 
print("\nCurrent items in Queue: ", QueueArray)

while True:
    print("\nWhat do you want to do? ")
    print("\n1. Add element in Queue.")
    print("2. Remove element from Queue.")
    print("3. Exit.")
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        InputString = input("Enter a string: ")
        ReturnValue, QueueArray, QueueHeadPointer, QueueTailPointer, NumberOfItems = Enqueue(QueueArray, QueueHeadPointer, QueueTailPointer, NumberOfItems, InputString)
        if ReturnValue == True:
            print("Insertion Successful!")
            print("Updated Queue is: ", QueueArray)
        else:
            print("Queue is Empty!")
    elif choice == 2:
        ReturnValue, QueueArray, QueueHeadPointer, QueueTailPointer, NumberOfItems = Dequeue(QueueArray, QueueHeadPointer, QueueTailPointer, NumberOfItems)
        print("String Removed: ", ReturnValue)
    elif choice == 3:
        break
    else:
        print("Invalid choice...")


