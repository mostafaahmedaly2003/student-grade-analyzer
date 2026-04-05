from typing import List, Optional

from student import Student
from analyzer import (
    calculate_average,
    calculate_median,
    calculate_std_dev,
    get_top_student,
    get_lowest_student,
    count_pass_fail,
    sort_by_grade,
    grade_distribution,
    get_class_gpa,
)

try:
    from colorama import init, Fore, Style

    init(autoreset=True)
    COLORS = True
except ImportError:
    COLORS = False

    class Fore:
        GREEN = RED = YELLOW = CYAN = MAGENTA = BLUE = WHITE = ""

    class Style:
        BRIGHT = RESET_ALL = ""


DIVIDER = "-" * 52
THICK_DIVIDER = "=" * 52


def color(text: str, fore: str = "", style: str = "") -> str:
    if COLORS:
        return f"{style}{fore}{text}{Style.RESET_ALL}"
    return text


def print_header(title: str):
    print(f"\n{color(THICK_DIVIDER, Fore.CYAN)}")
    print(color(f"  {title}", Fore.CYAN, Style.BRIGHT))
    print(color(THICK_DIVIDER, Fore.CYAN))


def print_menu():
    print(f"\n{color(THICK_DIVIDER, Fore.CYAN)}")
    print(color("   Student Grade Analyzer v2.0", Fore.CYAN, Style.BRIGHT))
    print(color(THICK_DIVIDER, Fore.CYAN))
    options = [
        ("1", "Add Students"),
        ("2", "View All Students"),
        ("3", "Search Student"),
        ("4", "Edit Student"),
        ("5", "Delete Student"),
        ("6", "Class Statistics"),
        ("7", "Export Report"),
        ("8", "Load from CSV"),
        ("9", "Exit"),
    ]
    for num, label in options:
        print(f"  {color(f'[{num}]', Fore.YELLOW, Style.BRIGHT)} {label}")
    print(color(THICK_DIVIDER, Fore.CYAN))


def _grade_color(grade: float) -> str:
    if grade >= 80:
        return Fore.GREEN
    elif grade >= 60:
        return Fore.YELLOW
    else:
        return Fore.RED


def print_student_card(student: Student, rank: Optional[int] = None):
    print(color(DIVIDER, Fore.WHITE))
    prefix = color(f"  #{rank}  ", Fore.CYAN, Style.BRIGHT) if rank else "  "
    print(f"{prefix}{color(student.name, Fore.WHITE, Style.BRIGHT)}")
    gc = _grade_color(student.grade)
    print(f"      Grade  : {color(f'{student.grade:.2f}', gc, Style.BRIGHT)}")
    print(f"      Letter : {color(student.letter, gc, Style.BRIGHT)}")
    print(f"      GPA    : {color(f'{student.gpa:.1f} / 4.0', gc)}")
    sc = Fore.GREEN if student.status == "Pass" else Fore.RED
    print(f"      Status : {color(student.status, sc, Style.BRIGHT)}")


def display_all_students(students: List[Student]):
    if not students:
        print(color("\n  No student data available.", Fore.YELLOW))
        return

    print_header(f"All Students  ({len(students)} total)")
    for student in students:
        print_student_card(student)
    print(color(DIVIDER, Fore.WHITE))

    print_header("Student Ranking")
    for i, student in enumerate(sort_by_grade(students), 1):
        gc = _grade_color(student.grade)
        medal = {1: "Gold  ", 2: "Silver", 3: "Bronze"}.get(i, f"#{i:<5}")
        print(
            f"  {color(medal, Fore.YELLOW)}  {student.name:<22}"
            f"  {color(f'{student.grade:.2f}', gc, Style.BRIGHT)}"
            f"  {color(student.letter, gc)}"
        )
    print(color(DIVIDER, Fore.WHITE))


def display_statistics(students: List[Student]):
    if not students:
        print(color("\n  No student data available.", Fore.YELLOW))
        return

    avg = calculate_average(students)
    median = calculate_median(students)
    std_dev = calculate_std_dev(students)
    top = get_top_student(students)
    lowest = get_lowest_student(students)
    pass_count, fail_count = count_pass_fail(students)
    dist = grade_distribution(students)
    class_gpa = get_class_gpa(students)
    total = len(students)
    pass_rate = (pass_count / total) * 100

    print_header("Class Statistics")
    print(f"  Total Students   : {color(str(total), Fore.CYAN, Style.BRIGHT)}")
    print(f"  Class Average    : {color(f'{avg:.2f}', Fore.CYAN, Style.BRIGHT)}")
    print(f"  Median Grade     : {color(f'{median:.2f}', Fore.CYAN)}")
    print(f"  Std Deviation    : {color(f'{std_dev:.2f}', Fore.CYAN)}")
    print(f"  Class GPA        : {color(f'{class_gpa:.2f} / 4.0', Fore.CYAN)}")
    print(f"  Top Student      : {color(top.name, Fore.GREEN, Style.BRIGHT)} ({color(f'{top.grade:.2f}', Fore.GREEN)})")
    print(f"  Lowest Student   : {color(lowest.name, Fore.RED, Style.BRIGHT)} ({color(f'{lowest.grade:.2f}', Fore.RED)})")
    print(f"  Passed           : {color(str(pass_count), Fore.GREEN, Style.BRIGHT)} / {total}  ({pass_rate:.1f}%)")
    print(f"  Failed           : {color(str(fail_count), Fore.RED, Style.BRIGHT)} / {total}  ({100 - pass_rate:.1f}%)")

    print_header("Grade Distribution")
    grade_colors = {
        "A": Fore.GREEN,
        "B": Fore.CYAN,
        "C": Fore.YELLOW,
        "D": Fore.MAGENTA,
        "F": Fore.RED,
    }
    for letter, count in dist.items():
        bar = "\u2588" * count
        pct = (count / total * 100) if total > 0 else 0
        col = grade_colors.get(letter, Fore.WHITE)
        print(f"  {color(letter, col, Style.BRIGHT)}  {color(bar if bar else '-', col)}  {color(f'{count} student(s)  ({pct:.1f}%)', col)}")
    print(color(DIVIDER, Fore.WHITE))


def display_search_results(matches: List[Student]):
    if not matches:
        print(color("\n  No students found matching that name.", Fore.RED))
        return
    print_header(f"Search Results  ({len(matches)} found)")
    for student in matches:
        print_student_card(student)
    print(color(DIVIDER, Fore.WHITE))
