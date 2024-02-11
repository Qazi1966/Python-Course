def bubblesort(array):
    has_swapped = True
    
    while(has_swapped):
        has_swapped = False
        for i in range(0, len(list1) - 1):
            if list1[i] > list1[i + 1]:
                # Swap
                temp = list1[i]
                list1[i] = list1[i + 1]
                list1[i + 1] = temp
                has_swapped = True
        return list1
    
list1 = (56, 26, 64, 92, 29, 35, 77)
print("The Unsorted list is: ", list1)
print("The Sorted list is: ", bubblesort(list1))

            