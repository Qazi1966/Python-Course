def linearsearch(arraydata, n, searchvalue):
    for i in range(0, n):
        if (arraydata[i] == searchvalue):
            return i
    return -1

arraydata = [10, 5, 6 , 7, 1, 12, 13, 15, 21, 8]
searchvalue = int(input("Enter Number to search: "))
n = len(arraydata)
result = linearsearch(arraydata, n, searchvalue)
if (result == -1):
    print("Not found")
else:
    print("Found at index:", result)

