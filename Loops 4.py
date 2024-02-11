for std in range(0, 10):
    stdname = input("Enter Student Name: ")
    mysum = 0
    for subj in range(0, 5, 1):
        marks = int(input("Enter Marks: "))
        mysum = mysum + marks
    print (stdname, " ", mysum)