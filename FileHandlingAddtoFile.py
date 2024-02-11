filename = "StudentDataFH.txt"
newfilename = "NewStudentDataFH.txt"
# WRITE FILE
def writeinfile():
    FileHandle = open(filename, "w")
    for i in range(5):
        stdname = input("Enter The Student's Name: ")
        FileHandle.write(stdname+"\n")
    FileHandle.close()

# READ FILE
def readfromfile():
    FileHandle = open(filename, "r")
    for x in range(5):
        stdrecord = FileHandle.readline()
        print(stdrecord)
    FileHandle.close()
    
def updatefilesequential():
    flag = True
    FileHandle1 = open(filename, "r")        
    FileHandle2 = open(newfilename, "w")
    newstdname = input("Enter new students name: ")
    stdrecord = FileHandle1.readline()
    while len(stdrecord) > 0 and flag:
        if stdrecord < newstdname:
            FileHandle2.write(stdrecord)
        else:
            FileHandle2.write(newstdname + "\n")
            FileHandle2.write(stdrecord)
            flag = False
        stdrecord = FileHandle1.readline()

    while len(stdrecord) > 0:
        FileHandle2.write(stdrecord)
        stdrecord = FileHandle1.readline()
    FileHandle1.close()
    FileHandle2.close()

# writeinfile()     
readfromfile()
updatefilesequential()