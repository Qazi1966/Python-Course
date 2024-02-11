def IDlinearsearch(arraydata, n, searchvalue):
    for i in range(0, n):
        if (arraydata[i] == searchvalue):
            return i
    return -1

stdID = [1, 2, 3, 4, 5]
stdname = ["Ali", "Rabeela", "Hussain", "Ibrahim", "Hamna"]

stdIDinput = int(input("Enter the StudentID: "))
stdIDindex = IDlinearsearch(stdID, 5, stdIDinput)
print(stdname[stdIDindex])



