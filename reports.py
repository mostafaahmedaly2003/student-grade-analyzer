import csv
import json
from typing import List

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

DIVIDER = "-" * 52


def load_from_csv(filename: str) -> List[Student]:
    students = []
    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    name = row["name"].strip().title()
                    grade = float(row["grade"])
                    if 0 <= grade <= 100:
                        students.append(Student(name=name, grade=grade))
                    else:
                        print(f"  Skipped {name}: grade {grade} is out of range.")
                except (ValueError, KeyError):
                    print(f"  Skipped invalid row: {row}")

        if students:
            print(f"\n  Loaded {len(students)} student(s) from '{filename}'")
        else:
            print(f"\n  No valid student data found in '{filename}'")

    except FileNotFoundError:
        print(f"\n  File '{filename}' not found.")

    return students


def save_txt_report(students: List[Student], filename: str = "report.txt"):
    avg = calculate_average(students)
    median = calculate_median(students)
    std_dev = calculate_std_dev(students)
    top = get_top_student(students)
    lowest = get_lowest_student(students)
    pass_count, fail_count = count_pass_fail(students)
    ranked = sort_by_grade(students)
    dist = grade_distribution(students)
    class_gpa = get_class_gpa(students)
    total = len(students)

    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 52 + "\n")
        f.write("        STUDENT GRADE ANALYZER REPORT\n")
        f.write("=" * 52 + "\n\n")

        f.write("=== Student Results ===\n")
        for s in students:
            f.write(DIVIDER + "\n")
            f.write(f"Name   : {s.name}\n")
            f.write(f"Grade  : {s.grade:.2f}\n")
            f.write(f"Letter : {s.letter}\n")
            f.write(f"GPA    : {s.gpa:.1f} / 4.0\n")
            f.write(f"Status : {s.status}\n")
        f.write(DIVIDER + "\n\n")

        f.write("=== Student Ranking ===\n")
        f.write(DIVIDER + "\n")
        for i, s in enumerate(ranked, 1):
            f.write(f"{i}. {s.name} - {s.grade:.2f} ({s.letter})\n")
        f.write(DIVIDER + "\n\n")

        f.write("=== Class Statistics ===\n")
        f.write(DIVIDER + "\n")
        f.write(f"Total Students   : {total}\n")
        f.write(f"Class Average    : {avg:.2f}\n")
        f.write(f"Median Grade     : {median:.2f}\n")
        f.write(f"Std Deviation    : {std_dev:.2f}\n")
        f.write(f"Class GPA        : {class_gpa:.2f} / 4.0\n")
        f.write(f"Top Student      : {top.name} ({top.grade:.2f})\n")
        f.write(f"Lowest Student   : {lowest.name} ({lowest.grade:.2f})\n")
        f.write(f"Passed           : {pass_count} ({pass_count / total * 100:.1f}%)\n")
        f.write(f"Failed           : {fail_count} ({fail_count / total * 100:.1f}%)\n")
        f.write(DIVIDER + "\n\n")

        f.write("=== Grade Distribution ===\n")
        f.write(DIVIDER + "\n")
        for letter, count in dist.items():
            pct = (count / total * 100) if total > 0 else 0
            bar = "#" * count
            f.write(f"  {letter}: {bar if bar else '-':<{total}}  {count} ({pct:.1f}%)\n")
        f.write(DIVIDER + "\n")

    print(f"\n  Report saved to '{filename}'")


def save_csv_report(students: List[Student], filename: str = "report.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "grade", "letter", "gpa", "status"])
        writer.writeheader()
        for s in students:
            writer.writerow(s.to_dict())
    print(f"\n  Report saved to '{filename}'")


def save_json_report(students: List[Student], filename: str = "report.json"):
    avg = calculate_average(students)
    median = calculate_median(students)
    std_dev = calculate_std_dev(students)
    top = get_top_student(students)
    lowest = get_lowest_student(students)
    pass_count, fail_count = count_pass_fail(students)
    class_gpa = get_class_gpa(students)
    dist = grade_distribution(students)
    total = len(students)

    data = {
        "students": [s.to_dict() for s in students],
        "statistics": {
            "total": total,
            "average": round(avg, 2),
            "median": round(median, 2),
            "std_deviation": round(std_dev, 2),
            "class_gpa": round(class_gpa, 2),
            "top_student": top.name if top else None,
            "lowest_student": lowest.name if lowest else None,
            "passed": pass_count,
            "failed": fail_count,
            "pass_rate": round((pass_count / total) * 100, 1) if total else 0,
            "grade_distribution": dist,
        },
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"\n  Report saved to '{filename}'")
