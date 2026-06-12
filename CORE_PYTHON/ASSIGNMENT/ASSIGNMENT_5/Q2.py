# ## Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(1, n + 1):
    print(f"Enter marks of student {i}")

    total_marks = 0

    for j in range(1, 6):
        marks = float(input(f"Subject {j} marks: "))
        total_marks += marks

    percentage = (total_marks / 500) * 100

    print("Percentage of Student", i, "=", percentage, "%")

    total_percentage += percentage

average_percentage = total_percentage / n

print("\nAverage Percentage of all students =", average_percentage, "%")