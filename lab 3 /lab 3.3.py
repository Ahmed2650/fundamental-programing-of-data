grades = input("Enter a list of students' grades separated by spaces: ").split()
count = 0
validlist = []
for grade in grades:
    if not (0 <= int(grade) <= 100):
        count += 1

        validlist.append(0)
    else:

        validlist.append(1)
if count > 0:
    print("Invalid","Number of invalid grades:",count)
else:
    print("All grades are valid")

    grades = [int(grade) for grade in grades]
    average = sum(grades) / len(grades)
    print("Average Grade:", average)

    maxgrade = max(grades)
    mingrade = min(grades)
    maxindex =grades.index(maxgrade)
    minindex =grades.index(mingrade)
    print("Highest Grade:", maxgrade, "at positions:", maxindex+1)
    print("Lowest Grade:", mingrade, "at positions:", minindex+1)

    above85 = 0
    for grade in grades:
        if grade > 85:
            above85 += 1

    print("students have grades greater than 85%.",above85)

    aboveaverage = 0
    for grade in grades:
        if grade > average:
            aboveaverage += 1

    print("students have grades greater than the average =",aboveaverage)
