def bubble_sort(arraydata):
    n = len(arraydata)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arraydata[j] > arraydata[j + 1]:
                arraydata[j], arraydata[j + 1] = arraydata[j + 1], arraydata[j]

def insertion_sort(arraydata):
    for i in range(1, len(arraydata)):
        key = arraydata[i]
        j = i - 1
        while j >= 0 and key < arraydata[j]:
            arraydata[j + 1] = arraydata[j]
            j -= 1
        arraydata[j + 1] = key

def linear_search(arraydata, searchvalue):
    for i in range(len(arraydata)):
        if arraydata[i] == searchvalue:
            return i
    return -1

def binary_search(arraydata, searchvalue):
    low = 0
    high = len(arraydata) - 1
    while low <= high:
        mid = (low + high) // 2
        if arraydata[mid] == searchvalue:
            return mid
        elif arraydata[mid] < searchvalue:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Input marks for 20 students
marks = []
for i in range(20):
   marks.append(int(input("Enter marks for student " + str(i + 1) + ": ")))

while True:
    print("\nOptions:")
    print("1. Sort marks (Bubble Sort)")
    print("2. Sort marks (Insertion Sort)")
    print("3. Search for a mark (Linear Search)")
    print("4. Search for a mark (Binary Search)")
    print("5. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        bubble_sort(marks)
        print("Marks sorted using Bubble Sort:", marks)
    elif choice == 2:
        insertion_sort(marks)
        print("Marks sorted using Insertion Sort:", marks)
    elif choice == 3:
        searchvalue = int(input("Enter the mark to search: "))
        index = linear_search(marks, searchvalue)
        if index != -1:
            print("Mark", searchvalue, "found at index", index)
        else:
            print("Mark", searchvalue, "not found in the list")
    elif choice == 4:
        searchvalue = int(input("Enter the mark to search: "))
        index = binary_search(marks, searchvalue)
        if index != -1:
            print("Mark", searchvalue, "found at index", index)
        else:
            print("Mark", searchvalue, "not found in the list")
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please select a valid option.")
