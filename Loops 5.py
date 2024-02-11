std = 0
while std < 10:
    stdname = input("Enter Student Marks: ")
    mysum = 0
    for subj in range(0, 5, 1):
        marks = int(input("Enter Marks: "))
        mysum = mysum + marks
    print(stdname, " ", mysum)
    std = std + 1
        