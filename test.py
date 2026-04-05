import unittest

from student import Student, get_letter_grade, get_gpa, get_status
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
    calculate_percentile,
)


class TestLetterGrade(unittest.TestCase):
    def test_a(self):
        self.assertEqual(get_letter_grade(100), "A")
        self.assertEqual(get_letter_grade(90), "A")

    def test_b(self):
        self.assertEqual(get_letter_grade(89), "B")
        self.assertEqual(get_letter_grade(80), "B")

    def test_c(self):
        self.assertEqual(get_letter_grade(79), "C")
        self.assertEqual(get_letter_grade(70), "C")

    def test_d(self):
        self.assertEqual(get_letter_grade(69), "D")
        self.assertEqual(get_letter_grade(60), "D")

    def test_f(self):
        self.assertEqual(get_letter_grade(59), "F")
        self.assertEqual(get_letter_grade(0), "F")


class TestGPA(unittest.TestCase):
    def test_values(self):
        self.assertEqual(get_gpa(95), 4.0)
        self.assertEqual(get_gpa(85), 3.0)
        self.assertEqual(get_gpa(75), 2.0)
        self.assertEqual(get_gpa(65), 1.0)
        self.assertEqual(get_gpa(50), 0.0)


class TestStatus(unittest.TestCase):
    def test_pass(self):
        self.assertEqual(get_status(60), "Pass")
        self.assertEqual(get_status(100), "Pass")

    def test_fail(self):
        self.assertEqual(get_status(59), "Fail")
        self.assertEqual(get_status(0), "Fail")


class TestStudentClass(unittest.TestCase):
    def test_properties(self):
        s = Student("Alice", 92)
        self.assertEqual(s.letter, "A")
        self.assertEqual(s.gpa, 4.0)
        self.assertEqual(s.status, "Pass")

    def test_to_dict(self):
        s = Student("Bob", 75)
        d = s.to_dict()
        self.assertEqual(d["name"], "Bob")
        self.assertEqual(d["grade"], 75)
        self.assertEqual(d["letter"], "C")
        self.assertEqual(d["gpa"], 2.0)
        self.assertEqual(d["status"], "Pass")


class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        self.students = [
            Student("Alice", 90),
            Student("Bob", 70),
            Student("Carol", 80),
            Student("David", 50),
            Student("Emma", 100),
        ]

    def test_average(self):
        self.assertAlmostEqual(calculate_average(self.students), 78.0)

    def test_average_empty(self):
        self.assertEqual(calculate_average([]), 0.0)

    def test_median_odd(self):
        self.assertAlmostEqual(calculate_median(self.students), 80.0)

    def test_median_even(self):
        two = [Student("A", 60), Student("B", 80)]
        self.assertAlmostEqual(calculate_median(two), 70.0)

    def test_std_dev(self):
        self.assertGreater(calculate_std_dev(self.students), 0)

    def test_std_dev_single(self):
        self.assertEqual(calculate_std_dev([Student("A", 80)]), 0.0)

    def test_top_student(self):
        self.assertEqual(get_top_student(self.students).name, "Emma")

    def test_lowest_student(self):
        self.assertEqual(get_lowest_student(self.students).name, "David")

    def test_top_lowest_empty(self):
        self.assertIsNone(get_top_student([]))
        self.assertIsNone(get_lowest_student([]))

    def test_pass_fail(self):
        pass_count, fail_count = count_pass_fail(self.students)
        self.assertEqual(pass_count, 4)
        self.assertEqual(fail_count, 1)

    def test_sort_by_grade(self):
        ranked = sort_by_grade(self.students)
        self.assertEqual(ranked[0].name, "Emma")
        self.assertEqual(ranked[-1].name, "David")

    def test_grade_distribution(self):
        dist = grade_distribution(self.students)
        self.assertEqual(dist["A"], 2)   # 90 and 100
        self.assertEqual(dist["B"], 1)   # 80
        self.assertEqual(dist["C"], 1)   # 70
        self.assertEqual(dist["F"], 1)   # 50
        self.assertEqual(dist["D"], 0)

    def test_class_gpa(self):
        gpa = get_class_gpa(self.students)
        self.assertGreater(gpa, 0)
        self.assertLessEqual(gpa, 4.0)

    def test_percentile(self):
        emma = self.students[4]  # grade 100
        pct = calculate_percentile(self.students, emma)
        self.assertEqual(pct, 80.0)  # 4 out of 5 students below her


if __name__ == "__main__":
    unittest.main(verbosity=2)
