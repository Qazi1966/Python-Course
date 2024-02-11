Queue = [-1 for i in range(20)]
HeadPointer = -1
TailPointer = 0

def Enqueue(Data):
    global Queue
    global HeadPointer
    global TailPointer
    
    if (TailPointer < 20):
        if HeadPointer == -1:
            HeadPointer = 0
        Queue[TailPointer] = Data
        TailPointer = TailPointer + 1
        return True
    return False

Success = False
for count in range(1,21):
    Success = Enqueue(count)
if (Success == False):
    print("Unsuccessful")
else:
    print("Successful")
    
count = 20
start = 1

# RECURSIVE SUM
def RecursiveOutput(start):
    if (start == 0):
        return Queue[start]
    else:
        return Queue[start] + RecursiveOutput(start - 1) 
print("Sum of queue using recursion is:", RecursiveOutput(TailPointer - 1))

# ITERATIVE SUM
def IterativeOutput():
    global start
    start = 20
    total = 0
    for x in range((start - 1), (HeadPointer -1), -1):
        total = total + Queue[x]
    return total
print("Sum of queue using iteration is:", IterativeOutput())
