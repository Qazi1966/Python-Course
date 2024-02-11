# Returns indenum of num in array if present, else -1
def binary_search(arrayay, low, high, num):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if array[mid] == num:
            return mid
 
        # If element is smaller than mid, then it can only be present in left subarray
        elif array[mid] > num:
            return binary_search(array, low, mid - 1, num)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(array, mid + 1, high, num)
 
    else:
        # Element is not present in the array
        return -1
 
# Test array
array = [ 2, 3, 4, 10, 40 ]
print("Current Array: ", array)
num = int(input("Enter a number to search: "))
 
# Function call
result = binary_search(array, 0, len(array)-1, num)
 
if result != -1:
    print("Element is present at index:", result)
else:
    print("Element not found!")