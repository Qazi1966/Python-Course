def bubblesort(array):
    
    for iter_num in range(len(array) - 1, 0, -1):
        for i in range(iter_num):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp

array = [12, 67, 37, 52, 82, 6, 29]
print("The Unsorted List is: ", array)
bubblesort(array)
print("The sorted list is: ", array)