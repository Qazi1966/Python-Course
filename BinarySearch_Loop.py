# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1
def binary_search(array, num):
	low = 0
	high = len(array) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		# If x is greater, ignore left half
		if array[mid] < num:
			low = mid + 1

		# If x is smaller, ignore right half
		elif array[mid] > num:
			high = mid - 1

		# means x is present at mid
		else:
			return mid

	# If we reach here, then the element was not present
	return -1


# Test array
array = [ 2, 3, 4, 10, 40 ]
print("Current array: ", array)
num = int(input("Enter a Number to search: "))

# Function call
result = binary_search(array, num)

if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
