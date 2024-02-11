
# WRITE FILE
FileHandle = open("StudentInfo.txt", "w")
for i in range(5):
    stdfnames = input("Enter The Student's First Name: ")
    stdID = input("Enter The StudentID: ")
    stdgender = input("Enter The Students Gender: ")
    FileHandle.write(stdID+stdfnames+stdgender+"\n")
FileHandle.close

# READ FILE
# FileName = "StudentInfo.txt"
# FileHandle = open(FileName, "r")
# for x in range(5):
#     stdrecord = FileHandle.readline()
#     print(stdrecord)
#     print(stdrecord[:5], " ", stdrecord[5:5+10], " ", stdrecord[15:15+1])
# FileHandle.close()