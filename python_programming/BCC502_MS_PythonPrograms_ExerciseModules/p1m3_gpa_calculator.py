"""Part 1, Module 3: Calculate a student's GPA."""


def calculate_gpa(grades):
    """Return the average of a list of grade points."""
    return sum(grades) / len(grades)


def main():
    grades = []
    for course in ("first", "second", "third"):
        grades.append(float(input(f"Enter the grade points for the {course} course: ")))
    gpa = calculate_gpa(grades)
    print(f"Your GPA is {gpa:.2f}")


if __name__ == "__main__":
    main()
