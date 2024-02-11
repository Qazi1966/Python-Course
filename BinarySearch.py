def binarysearch(array, num, low, high):
    
    # Repeat until pointer Low and High meet each other
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == num:
            return mid
        
        elif array[mid] < num:
            low = mid + 1
            
        else:
            high = mid - 1
    return -1

array = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
num = int(input("Enter a Number to search: "))

result = binarysearch(array, num, 0, len(array) - 1)
if result != -1:
    print("Number is present at index: ", result)
else:
    print("Number Not Found")
        
