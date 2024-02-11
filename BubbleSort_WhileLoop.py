def bubblesort(array):
    i = 0
    j = 0  
    
    # Loop to access each array element (Number Of Passes)
    while i <= len(array):
        
        # Loop to compare array elements (Number Of Comparisons)
        while j < (len(array) - i - 1):
            
            # Compare two adjacent elements
            # Change > to < to sort in descending order
            if array[j] > array[j + 1]:
                
                # Swapping elements if elements are not in intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
            j = j + 1
        i = i + 1    
data = [12, 45, 0, 11, -9]
bubblesort(data)
namedata = ["Ali", "Hamna", "Tayyab", "Rabila", "Hussain", "Aimal", "Eshaal"]
bubblesort(namedata)
print("Sorted array in ascending order", data)
print("Sorted array in ascending order", namedata)

            
            
