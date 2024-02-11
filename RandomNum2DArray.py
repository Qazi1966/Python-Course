import random
arraydata = [[0] * 10 for i in range(10)]

for x in range(0, 10):
    for y in range(0, 10):
        print(arraydata[x][y], "", end = '')
    print()

print()

for x in range(0, 10):
    for y in range(0, 10):
        arraydata[x][y] = random.randint(1, 100)
        
for x in range(0, 10):
    for y in range(0, 10):
        print(arraydata[x][y], "", end = '')
    print()  
    
print()    # New Line

for x in range(0, 10):
    rowsum = 0
    rowmax = 0
    rowmin = 100
    for y in range(0, 10):
        rowsum = rowsum + arraydata[x][y]
        if arraydata[x][y] > rowmax:
            rowmax = arraydata[x][y]
        if arraydata[x][y] < rowmin:
            rowmin = arraydata[x][y]
    print("For Row No.", x)
    print("Sum Of Marks: ", rowsum)
    print("Maximum Marker: ", rowmax)
    print("Minimum Marker: ", rowmin)
    print()
    