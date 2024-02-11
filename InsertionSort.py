def insertionsort(list):
    for pointer in range(1, len(list)):
        itemtobeinserted = list[pointer]
        currentitem = pointer - 1

        while currentitem >= 0 and itemtobeinserted < list[currentitem]:
            list[currentitem + 1] = list[currentitem]
            currentitem = currentitem  - 1
            
        list[currentitem + 1] = itemtobeinserted
        
data = [9, 5, 1, 4, 3]
namedata = ["Ali", "Rabeela", "Hussain", "Eshaal", "Hamna", "Ibrahim", "Tayyab"]
print("Unsorted Integer Array: ", data)
insertionsort(data)
print("Sorted Integer Array in Ascending order: ", data)

print("Unsorted Names Array: ", namedata)
insertionsort(namedata)
print("Sorted Names Array in Ascending order: ", namedata)