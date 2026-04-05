import csv


def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def get_status(score):
    if score >= 60:
        return "Pass"
    return "Fail"


def get_student_data():
    students = []

    while True:
        try:
            num_students = int(input("Enter number of students: "))
            if num_students <= 0:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    for i in range(num_students):
        print(f"\nStudent {i + 1}")
        name = input("Enter student name: ").strip().title()

        while True:
            try:
                grade = float(input("Enter student grade (0 - 100): "))
                if 0 <= grade <= 100:
                    break
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        student = {
            "name": name,
            "grade": grade,
            "letter": get_letter_grade(grade),
            "status": get_status(grade)
        }

        students.append(student)

    return students


def calculate_average(students):
    if len(students) == 0:
        return 0

    total = 0
    for student in students:
        total += student["grade"]
    return total / len(students)


def get_top_student(students):
    if len(students) == 0:
        return None

    top_student = students[0]
    for student in students:
        if student["grade"] > top_student["grade"]:
            top_student = student
    return top_student


def get_lowest_student(students):
    if len(students) == 0:
        return None

    lowest_student = students[0]
    for student in students:
        if student["grade"] < lowest_student["grade"]:
            lowest_student = student
    return lowest_student


def count_pass_fail(students):
    pass_count = 0
    fail_count = 0

    for student in students:
        if student["grade"] >= 60:
            pass_count += 1
        else:
            fail_count += 1

    return pass_count, fail_count


def sort_students_by_grade(students):
    return sorted(students, key=lambda x: x["grade"], reverse=True)


def search_student(students):
    if len(students) == 0:
        print("\nNo student data available.")
        return

    print("\n=== Student Search ===")
    name = input("Enter student name to search: ").strip().title()

    found = False

    for student in students:
        if student["name"] == name:
            print("-" * 40)
            print(f"Name   : {student['name']}")
            print(f"Grade  : {student['grade']:.2f}")
            print(f"Letter : {student['letter']}")
            print(f"Status : {student['status']}")
            print("-" * 40)
            found = True
            break

    if not found:
        print("Student not found.")


def display_results(students):
    if len(students) == 0:
        print("\nNo student data available to display.")
        return

    print("\n=== Student Results ===")

    for student in students:
        print("-" * 40)
        print(f"Name   : {student['name']}")
        print(f"Grade  : {student['grade']:.2f}")
        print(f"Letter : {student['letter']}")
        print(f"Status : {student['status']}")
    print("-" * 40)

    sorted_students = sort_students_by_grade(students)

    print("\n=== Student Ranking ===")
    print("-" * 40)
    for i, student in enumerate(sorted_students, start=1):
        print(f"{i}. {student['name']} - {student['grade']:.2f}")
    print("-" * 40)

    average = calculate_average(students)
    top_student = get_top_student(students)
    lowest_student = get_lowest_student(students)
    pass_count, fail_count = count_pass_fail(students)

    print("\n=== Class Summary ===")
    print("-" * 40)
    print(f"Class Average    : {average:.2f}")
    print(f"Top Student      : {top_student['name']} ({top_student['grade']:.2f})")
    print(f"Lowest Student   : {lowest_student['name']} ({lowest_student['grade']:.2f})")
    print(f"Passed Students  : {pass_count}")
    print(f"Failed Students  : {fail_count}")
    print("-" * 40)


def save_report(students):
    if len(students) == 0:
        print("\nNo student data available to save.")
        return

    average = calculate_average(students)
    top_student = get_top_student(students)
    lowest_student = get_lowest_student(students)
    pass_count, fail_count = count_pass_fail(students)
    sorted_students = sort_students_by_grade(students)

    with open("report.txt", "w", encoding="utf-8") as file:
        file.write("=== Student Results ===\n")

        for student in students:
            file.write("-" * 40 + "\n")
            file.write(f"Name   : {student['name']}\n")
            file.write(f"Grade  : {student['grade']:.2f}\n")
            file.write(f"Letter : {student['letter']}\n")
            file.write(f"Status : {student['status']}\n")

        file.write("-" * 40 + "\n")

        file.write("\n=== Student Ranking ===\n")
        file.write("-" * 40 + "\n")
        for i, student in enumerate(sorted_students, start=1):
            file.write(f"{i}. {student['name']} - {student['grade']:.2f}\n")
        file.write("-" * 40 + "\n")

        file.write("\n=== Class Summary ===\n")
        file.write("-" * 40 + "\n")
        file.write(f"Class Average    : {average:.2f}\n")
        file.write(f"Top Student      : {top_student['name']} ({top_student['grade']:.2f})\n")
        file.write(f"Lowest Student   : {lowest_student['name']} ({lowest_student['grade']:.2f})\n")
        file.write(f"Passed Students  : {pass_count}\n")
        file.write(f"Failed Students  : {fail_count}\n")
        file.write("-" * 40 + "\n")

    print("\nReport saved successfully to report.txt")


def load_students_from_csv(filename):
    students = []

    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    name = row["name"].strip().title()
                    grade = float(row["grade"])

                    if 0 <= grade <= 100:
                        student = {
                            "name": name,
                            "grade": grade,
                            "letter": get_letter_grade(grade),
                            "status": get_status(grade)
                        }
                        students.append(student)
                    else:
                        print(f"Skipped invalid grade for {name}: {grade}")

                except (ValueError, KeyError, TypeError):
                    print(f"Skipped invalid row: {row}")

        if len(students) > 0:
            print(f"\nLoaded {len(students)} students from {filename}")
        else:
            print(f"\nNo valid student data found in {filename}")

    except FileNotFoundError:
        print(f"\nFile '{filename}' not found.")

    return students


def main():
    print("=== Student Grade Analyzer ===")

    while True:
        choice = input("Load students from CSV file? (y/n): ").strip().lower()

        if choice == "y":
            students = load_students_from_csv("students.csv")
            break
        elif choice == "n":
            students = get_student_data()
            break
        else:
            print("Please enter y or n.")

    if len(students) == 0:
        print("\nNo student data available. Program will exit.")
        return

    display_results(students)

    while True:
        search_choice = input("\nDo you want to search for a student? (y/n): ").strip().lower()

        if search_choice == "y":
            search_student(students)
        elif search_choice == "n":
            break
        else:
            print("Please enter y or n.")

    while True:
        save_choice = input("\nDo you want to save the report to a file? (y/n): ").strip().lower()

        if save_choice == "y":
            save_report(students)
            break
        elif save_choice == "n":
            break
        else:
            print("Please enter y or n.")

    print("\nProgram finished.")


if __name__ == "__main__":
    main()