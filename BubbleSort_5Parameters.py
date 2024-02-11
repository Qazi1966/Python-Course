def bubblesort(array):
    
    # Loop to access each array element (Number Of Passes)
    for i in range(len(array)):
        
        # Loop to compare array elements (Number Of Comparisons)
        for j in range(0, len(array) - i - 1):
            
            # Compare two adjacent elements
            # Change > to < to sort in descending order
            if array[j] > array[j + 1]:
                
                # Swapping elements if elements are not in intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                
data = [12, 45, 0, 11, -9]
bubblesort(data)
namedata = ["Ali", "Hamna", "Tayyab", "Rabila", "Hussain", "Aimal", "Eshaal"]
bubblesort(namedata)
realdata = [12.2, 45.7, 35.9, 83.9, 8.87]
bubblesort(realdata)
chardata = ["A", "g", "k", "L", "W", "o"]
bubblesort(chardata)
print("Sorted Integer array in ascending order", data)
print("Sorted Name array in ascending order", namedata)
print("Sorted Real array in ascending order", realdata)
print("Sorted Char array in ascending order", chardata)

            
            
