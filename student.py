from dataclasses import dataclass


def get_letter_grade(score: float) -> str:
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


def get_gpa(score: float) -> float:
    if score >= 90:
        return 4.0
    elif score >= 80:
        return 3.0
    elif score >= 70:
        return 2.0
    elif score >= 60:
        return 1.0
    else:
        return 0.0


def get_status(score: float) -> str:
    return "Pass" if score >= 60 else "Fail"


@dataclass
class Student:
    name: str
    grade: float

    @property
    def letter(self) -> str:
        return get_letter_grade(self.grade)

    @property
    def gpa(self) -> float:
        return get_gpa(self.grade)

    @property
    def status(self) -> str:
        return get_status(self.grade)

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "grade": self.grade,
            "letter": self.letter,
            "gpa": self.gpa,
            "status": self.status,
        }
