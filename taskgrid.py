import random
taskgrid = [[False] * 10 for i in range(8)]     # Initialises all the values by false
for x in range(8):
    for y in range(10):
        print(taskgrid[x][y], "", end= '')
    print()
completed = 0
while completed != 80:  # Total Number Of Attempts are 60
    NewSaffTask = False
    while NewSaffTask == False:     # To ensure that values are not repeated
        row = random.randint(0, 7)
        col = random.randint(0, 9)
        if taskgrid[row][col] == False:
            taskgrid[row][col] = True
            NewSaffTask = True
    completed = completed + 1

print()
print()

for x in range(8):
    for y in range(10):
        print(taskgrid[x][y], "", end= '')
    print()
    
        
    