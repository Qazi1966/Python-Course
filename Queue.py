def enqueue(queue, head, tail, numitems, inputdata):
    if numitems>= 10:
        return (False, head, tail, numitems)
    queue[tail] = inputdata
    if tail >= 9:
        tail = 0
    else:
        tail = tail + 1
    numitems = numitems + 1
    return (True, queue, head, tail, inputdata)

def dequeue(queue, head, tail ,numitems):
    if numitems == 0:
        return (False, queue, head, tail, numitems)
    else:
        returnvalue = queue[head]
        head = head + 1
        if head >= 9:
            head = 0
            numitems = numitems - 1
        return(returnvalue, queue, head, tail, numitems)

queuearray = [""] * 10
headpointer = 0   
tailpointer = 0
numberofitems = 0

for i in range(0, 11):
    inputstring = input("Enter A String: ")
    returnvalue, queuearray, headpointer, tailpointer, numberofitems, inputstring = enqueue(queuearray, headpointer, tailpointer, numberofitems, inputstring)
    if returnvalue == True:
        print("Successful")
    else:
        print("Unsuccessful")

returnvalue, queuearray, headpointer, tailpointer, numberofitems = dequeue(queuearray, headpointer, tailpointer, numberofitems) 
print(returnvalue)