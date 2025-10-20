def calculate_grade(*marks):
    # Calculate the average marks
    average = sum(marks) / len(marks)

    # Determine the grade based on the average
    if average >= 75:
        grade = "Distinction"
    elif average >= 60:
        grade = "First Class"
    elif average >= 40:
        grade = "Pass"
    else:
        grade = "Fail"

    return grade, average


marks = list(map(int, input("Enter marks for each subject separated by space: ").split()))
grade, average = calculate_grade(*marks)
print(f"Average marks: {average:.2f}")
print(f"Grade: {grade}")