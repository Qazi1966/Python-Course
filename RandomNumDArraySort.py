import random

arraydata = [[0] * 10 for i in range(10)]

# Initialize the array with random integers
for x in range(10):
    for y in range(10):
        arraydata[x][y] = random.randint(1, 100)

# Print the original array
for x in range(10):
    for y in range(10):
        print(arraydata[x][y], "", end='')
    print()

print()  # New Line

# Sort each row in ascending order
arraylength = 10
for x in range(arraylength):
    for y in range(arraylength - 1):
        for z in range(arraylength - y - 1):
            if arraydata[x][z] > arraydata[x][z + 1]:
                # Swap the elements
                temp = arraydata[x][z]
                arraydata[x][z] = arraydata[x][z + 1]
                arraydata[x][z + 1] = temp

# Print the sorted array
for x in range(10):
    for y in range(10):
        print(arraydata[x][y], "", end='')
    print()
