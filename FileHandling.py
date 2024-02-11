# # APPEND FILE
# FileHandle = open("StudentFH.txt", "a")
# for i in range(3):
#     stdfnames = input("Enter The Student's First Name: ")
#     stdlnames = input("Enter The Student's Last Name: ")
#     FileHandle.write(stdfnames+stdlnames)
# FileHandle.close

# WRITE FILE
FileHandle = open("StudentFH.txt", "w")
for i in range(3):
    stdfnames = input("Enter The Student's First Name: ")
    stdlnames = input("Enter The Student's Last Name: ")
    FileHandle.write(stdfnames+stdlnames)
FileHandle.close

# READ FILE
# FileHandle = open("StudentFH.txt", "r")
# FullName = FileHandle.readline()
# while len(FullName) > 0:
#     print(FullName, "")
#     FullName = FileHandle.readline()
# FileHandle.close()

# READ FILE ALTERNATIVE
# FileHandle = open("StudentFH.txt", "r")
# for line in FileHandle:
#     print(line)
# FileHandle.close