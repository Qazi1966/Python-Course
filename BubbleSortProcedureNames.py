def bubblesort(array):
    
    for iter_num in range(len(array) - 1, 0, -1):
        for i in range(iter_num):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp

array = ["Ali", "Rabeela", "Hussain", "Hamna", "Eshaal", "Ibrahim"]
print("The Unsorted List is: ", array)
bubblesort(array)
print("The sorted list is: ", array)