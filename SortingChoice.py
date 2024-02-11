def bubblesort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                
def insertionsort(list):
    for pointer in range(1, len(list)):
        itemtobeinserted = list[pointer]
        currentitem = pointer - 1

        while currentitem >= 0 and itemtobeinserted < list[currentitem]:
            list[currentitem + 1] = list[currentitem]
            currentitem = currentitem  - 1
            
        list[currentitem + 1] = itemtobeinserted
        
data = [9, 5, 1, 4, 3, 56, 78, 37, 29, 56]
namedata = ["Ali", "Rabeela", "Hussain", "Eshaal", "Hamna", "Ibrahim", "Tayyab"]

choice = int(input("Press 1 For Bubble sort, Press 2 for Insertion Sort: "))

if choice == 1:
    print("Unsorted Integer Array: ", data)
    bubblesort(data)
    print("Sorted Integer Array in Ascending order: ", data)

    print("Unsorted Names Array: ", namedata)
    bubblesort(namedata)
    print("Sorted Names Array in Ascending order: ", namedata)
else:
    print("Unsorted Integer Array: ", data)
    insertionsort(data)
    print("Sorted Integer Array in Ascending order: ", data)

    print("Unsorted Names Array: ", namedata)
    insertionsort(namedata)
    print("Sorted Names Array in Ascending order: ", namedata)