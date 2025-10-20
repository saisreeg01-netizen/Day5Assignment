def student_info(**data):
    # Print all student details
    for key, value in data.items():
        print(f"{key.capitalize()}: {value}")

    # Check if grade is available
    if "grade" not in data:
        print("Grade: Grade not available")


# Example usage:
student_info(name="John Doe", age=20, grade="A", course="BCA")
print("\n")
student_info(name="Jane Doe", age=22, course="BBA")
