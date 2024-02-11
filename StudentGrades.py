paper1 = []
paper2 = []
percentagemarks = []
stdname = []
total = []
grade = []

paper1 = [0 for i in range(0 , 5)]
paper2 = [0 for i in range(0 , 5)]
percentagemarks = [0 for i in range(0 , 5)]
total = [0 for i in range(0 , 5)]
grade = ["" for i in range(0 , 5)]
stdname = ["" for i in range(0 , 5)]

for i in range (0 , 5):
    stdname[i] = input("Enter the name of Student: ")
    paper1[i] = int(input("Enter the marks for Paper1: "))
    paper2[i] = int(input("Enter the marks for Paper2: "))
    total[i] = paper1[i] + paper2[i]
    percentagemarks[i] = int((total[i]/150) * 100)
    
    if (percentagemarks[i] >= 90 and percentagemarks[i] <= 100):
        grade[i] = "A*"
    elif (percentagemarks[i] >= 80 and percentagemarks[i] <= 89):
        grade[i] = "A"
    elif (percentagemarks[i] >= 70 and percentagemarks[i] <= 79):
        grade[i] = "B"
    elif (percentagemarks[i] >= 60 and percentagemarks[i] <= 69):
        grade[i] = "C"
    elif (percentagemarks[i] >= 50 and percentagemarks[i] <= 59):
        grade[i] = "D"
    elif (percentagemarks[i] >= 45 and percentagemarks[i] <= 49):
        grade[i] = "E"
    else:    
        grade[i] = "U"
        
print(paper1)
print(paper2)
print(total)
print(percentagemarks)
print(grade)