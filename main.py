from student import Student
from display import (
    Fore,
    Style,
    color,
    print_header,
    print_menu,
    display_all_students,
    display_statistics,
    display_search_results,
)
from reports import (
    load_from_csv,
    save_txt_report,
    save_csv_report,
    save_json_report,
)


# ---------------------------------------------------------------------------
# Input helpers
# ---------------------------------------------------------------------------

def get_valid_grade(prompt: str) -> float:
    while True:
        try:
            grade = float(input(prompt))
            if 0 <= grade <= 100:
                return grade
            print(color("  Grade must be between 0 and 100.", Fore.RED))
        except ValueError:
            print(color("  Invalid input. Please enter a number.", Fore.RED))


def get_valid_int(prompt: str, min_val: int = 1) -> int:
    while True:
        try:
            val = int(input(prompt))
            if val >= min_val:
                return val
            print(color(f"  Please enter a number >= {min_val}.", Fore.RED))
        except ValueError:
            print(color("  Invalid input. Please enter a whole number.", Fore.RED))


def confirm(prompt: str) -> bool:
    while True:
        choice = input(prompt + " (y/n): ").strip().lower()
        if choice == "y":
            return True
        if choice == "n":
            return False
        print(color("  Please enter y or n.", Fore.RED))


# ---------------------------------------------------------------------------
# Menu actions
# ---------------------------------------------------------------------------

def add_students(students: list) -> list:
    print_header("Add Students")
    num = get_valid_int("  How many students to add? ", min_val=1)

    for i in range(num):
        print(f"\n  {color(f'Student {i + 1}', Fore.CYAN, Style.BRIGHT)}")
        name = input("  Name: ").strip().title()
        if not name:
            print(color("  Name cannot be empty. Skipping.", Fore.RED))
            continue
        grade = get_valid_grade("  Grade (0-100): ")
        students.append(Student(name=name, grade=grade))
        print(color(f"  + {name} added.", Fore.GREEN))

    return students


def search_student(students: list):
    print_header("Search Student")
    if not students:
        print(color("  No students to search.", Fore.YELLOW))
        return

    query = input("  Enter name (or partial name): ").strip().lower()
    matches = [s for s in students if query in s.name.lower()]
    display_search_results(matches)


def edit_student(students: list) -> list:
    print_header("Edit Student")
    if not students:
        print(color("  No students to edit.", Fore.YELLOW))
        return students

    for i, s in enumerate(students, 1):
        print(f"  {color(str(i) + '.', Fore.CYAN)} {s.name}  ({s.grade:.2f})")

    try:
        idx = int(input("\n  Select student number: ")) - 1
        if not (0 <= idx < len(students)):
            print(color("  Invalid selection.", Fore.RED))
            return students

        student = students[idx]
        print(f"\n  Editing: {color(student.name, Fore.WHITE, Style.BRIGHT)}")

        new_name = input(f"  New name (Enter to keep '{student.name}'): ").strip()
        if new_name:
            students[idx].name = new_name.title()

        if confirm("  Change grade?"):
            students[idx].grade = get_valid_grade("  New grade (0-100): ")

        print(color("  Student updated successfully.", Fore.GREEN))

    except ValueError:
        print(color("  Invalid input.", Fore.RED))

    return students


def delete_student(students: list) -> list:
    print_header("Delete Student")
    if not students:
        print(color("  No students to delete.", Fore.YELLOW))
        return students

    for i, s in enumerate(students, 1):
        print(f"  {color(str(i) + '.', Fore.CYAN)} {s.name}  ({s.grade:.2f})")

    try:
        idx = int(input("\n  Select student number to delete: ")) - 1
        if not (0 <= idx < len(students)):
            print(color("  Invalid selection.", Fore.RED))
            return students

        removed = students[idx]
        if confirm(f"  Delete {removed.name}?"):
            students.pop(idx)
            print(color(f"  {removed.name} removed.", Fore.GREEN))
        else:
            print(color("  Deletion cancelled.", Fore.YELLOW))

    except ValueError:
        print(color("  Invalid input.", Fore.RED))

    return students


def export_report(students: list):
    print_header("Export Report")
    if not students:
        print(color("  No students to export.", Fore.YELLOW))
        return

    print(f"  {color('[1]', Fore.YELLOW)} Text file  (.txt)")
    print(f"  {color('[2]', Fore.YELLOW)} CSV file   (.csv)")
    print(f"  {color('[3]', Fore.YELLOW)} JSON file  (.json)")
    print(f"  {color('[4]', Fore.YELLOW)} All formats")

    choice = input("\n  Choose format: ").strip()
    if choice == "1":
        save_txt_report(students)
    elif choice == "2":
        save_csv_report(students)
    elif choice == "3":
        save_json_report(students)
    elif choice == "4":
        save_txt_report(students)
        save_csv_report(students)
        save_json_report(students)
    else:
        print(color("  Invalid choice.", Fore.RED))


def load_csv(students: list) -> list:
    print_header("Load from CSV")
    filename = input("  CSV filename (Enter for 'students.csv'): ").strip()
    if not filename:
        filename = "students.csv"

    loaded = load_from_csv(filename)
    if not loaded:
        return students

    if students and confirm(f"  Merge with existing {len(students)} student(s)?"):
        students.extend(loaded)
    else:
        students = loaded

    return students


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    students = []

    while True:
        print_menu()
        choice = input("  Select option: ").strip()

        if choice == "1":
            students = add_students(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            students = edit_student(students)
        elif choice == "5":
            students = delete_student(students)
        elif choice == "6":
            display_statistics(students)
        elif choice == "7":
            export_report(students)
        elif choice == "8":
            students = load_csv(students)
        elif choice == "9":
            print(color("\n  Goodbye! Thanks for using Student Grade Analyzer.\n", Fore.CYAN, Style.BRIGHT))
            break
        else:
            print(color("\n  Invalid option. Please choose 1-9.", Fore.RED))

        input(color("\n  Press Enter to continue...", Fore.WHITE))


if __name__ == "__main__":
    main()
