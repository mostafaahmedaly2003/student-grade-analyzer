import math
from typing import List, Optional, Tuple

from student import Student


def calculate_average(students: List[Student]) -> float:
    if not students:
        return 0.0
    return sum(s.grade for s in students) / len(students)


def calculate_median(students: List[Student]) -> float:
    if not students:
        return 0.0
    grades = sorted(s.grade for s in students)
    n = len(grades)
    mid = n // 2
    if n % 2 == 0:
        return (grades[mid - 1] + grades[mid]) / 2
    return grades[mid]


def calculate_std_dev(students: List[Student]) -> float:
    if len(students) < 2:
        return 0.0
    avg = calculate_average(students)
    variance = sum((s.grade - avg) ** 2 for s in students) / len(students)
    return math.sqrt(variance)


def get_top_student(students: List[Student]) -> Optional[Student]:
    if not students:
        return None
    return max(students, key=lambda s: s.grade)


def get_lowest_student(students: List[Student]) -> Optional[Student]:
    if not students:
        return None
    return min(students, key=lambda s: s.grade)


def count_pass_fail(students: List[Student]) -> Tuple[int, int]:
    pass_count = sum(1 for s in students if s.grade >= 60)
    return pass_count, len(students) - pass_count


def sort_by_grade(students: List[Student]) -> List[Student]:
    return sorted(students, key=lambda s: s.grade, reverse=True)


def grade_distribution(students: List[Student]) -> dict:
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for s in students:
        dist[s.letter] += 1
    return dist


def calculate_percentile(students: List[Student], student: Student) -> float:
    if not students:
        return 0.0
    below = sum(1 for s in students if s.grade < student.grade)
    return (below / len(students)) * 100


def get_class_gpa(students: List[Student]) -> float:
    if not students:
        return 0.0
    return sum(s.gpa for s in students) / len(students)
