# Student Grade Analyzer

A Python CLI tool for managing and analyzing student grades — built with clean modular code, colored terminal output, statistics, and multi-format report export.

## Features

- **Interactive menu** — add, edit, delete, and search students
- **Colored terminal output** — grades highlighted green/yellow/red
- **Grade statistics** — average, median, standard deviation, GPA (4.0 scale)
- **Grade distribution chart** — visual ASCII bar chart per letter grade
- **Student ranking** — sorted leaderboard with medal positions
- **Partial name search** — find students by full or partial name
- **CSV import** — bulk load students from a CSV file
- **Multi-format export** — save reports as `.txt`, `.csv`, or `.json`
- **Unit tested** — core logic covered with `unittest`

## Project Structure

```
student-grade-analyzer/
├── main.py               # Entry point & interactive menu
├── student.py            # Student class + grade/GPA helpers
├── analyzer.py           # Statistics calculations
├── display.py            # Colored terminal UI
├── reports.py            # File I/O (CSV import, TXT/CSV/JSON export)
├── test.py               # Unit tests
├── sample_students.csv   # Sample data to try right away
├── requirements.txt
└── .gitignore
```

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/student-grade-analyzer.git
cd student-grade-analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> `colorama` is the only dependency — it adds colored output on Windows, macOS, and Linux. The program works without it too (colors are just skipped).

### 3. Run the program

```bash
python main.py
```

## Usage

On launch you get a numbered menu:

```
====================================================
   Student Grade Analyzer v2.0
====================================================
  [1] Add Students
  [2] View All Students
  [3] Search Student
  [4] Edit Student
  [5] Delete Student
  [6] Class Statistics
  [7] Export Report
  [8] Load from CSV
  [9] Exit
====================================================
```

### Load the sample data

Choose **[8] Load from CSV** and press Enter to load `sample_students.csv` (15 pre-built students) and explore all features instantly.

### CSV format

```csv
name,grade
Alice Johnson,92
Bob Smith,75
```

### Export formats

| Format | File | Contents |
|--------|------|----------|
| Text | `report.txt` | Full human-readable report |
| CSV | `report.csv` | Spreadsheet-ready student data |
| JSON | `report.json` | Students + full statistics object |

## Grade Scale

| Letter | Range | GPA |
|--------|-------|-----|
| A | 90 – 100 | 4.0 |
| B | 80 – 89  | 3.0 |
| C | 70 – 79  | 2.0 |
| D | 60 – 69  | 1.0 |
| F | 0 – 59   | 0.0 |

> Pass threshold: 60 and above.

## Running Tests

```bash
python -m unittest test.py -v
```

## Requirements

- Python 3.8+
- colorama (optional, for colored output)

## License

MIT License — feel free to use, modify, and share.
