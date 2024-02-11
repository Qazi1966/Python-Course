Jobs = [[0] * 2 for i in range(0, 10)]
NumberOfjobs = 0
    
def Initialise(arraydata):
    global Jobs
    global NumberOfjobs
    for x in range(0, 10):
        Jobs.append([-1, -1])
        NumberOfjobs = 0
        print(Jobs)

def AddJob(JobNumber, Priority):
    global NumberOfjobs
    global Jobs
    if NumberOfjobs == 10:
        print("Unsucessful!")
    else:
        # Jobs[NumberOfjobs] = [JobNumber, Priority]
        Jobs[NumberOfjobs][0] = -1
        Jobs[NumberOfjobs][1] = -1
        print("Successfully Added!")
        NumberOfjobs = NumberOfjobs + 1
        
def InsertionSort():
    global Jobs
    global NumberOfjobs
    for pointer in range(1, NumberOfjobs):
        CurrentJob = Jobs[pointer][0]
        CurrentPriority = Jobs[pointer][1]

        while pointer > 0 and Jobs[pointer - 1][1] > CurrentPriority:
            Jobs[pointer][0] = Jobs[pointer - 1][0]
            Jobs[pointer][1] = Jobs[pointer - 1][1]
            Jobs[pointer][0] = CurrentJob
            Jobs[pointer][1] = CurrentPriority

def BubbleSort(array):
    for i in range(2):
        swapped = False

        for j in range(0, len(array)-i-1):
            if array[j][1] > array[j+1][1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
            else:
                break

def PrintArray():
    global Jobs
    global NumberOfjobs
    for x in range(0, NumberOfjobs):
        print("Job Number: ", Jobs[x][0])
        print("Job Priority: ", Jobs[x][1])
        
while True:
    Initialise(Jobs)
    print("\nWhat do you want to do? ")
    print("\n1. Insertion Sort.")
    print("2. Bubble Sort.")
    print("3. Exit.")
    choice = int(input("\nEnter your choice: "))
    if choice == 1:
        InsertionSort(Jobs)
        print(Jobs)
    elif choice == 2:
        BubbleSort(Jobs)
        print(Jobs)
    elif choice == 3:
        break