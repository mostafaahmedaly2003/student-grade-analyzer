# Student Grade Analyzer

A Python project for managing and analyzing student grades — featuring a colorful CLI tool and an interactive web dashboard built with Streamlit.

## Features

- **Web dashboard** — interactive charts, rankings, search, and export in the browser
- **Interactive CLI** — add, edit, delete, and search students in the terminal
- **Colored terminal output** — grades highlighted green/yellow/red
- **Grade statistics** — average, median, standard deviation, GPA (4.0 scale)
- **Grade distribution chart** — visual bar chart per letter grade
- **Student ranking** — sorted leaderboard with medal positions
- **Partial name search** — find students by full or partial name
- **CSV import** — bulk load students from a CSV file
- **Multi-format export** — save reports as `.txt`, `.csv`, or `.json`
- **Unit tested** — core logic covered with `unittest`

## Project Structure

```
student-grade-analyzer/
├── dashboard.py          # Streamlit web dashboard
├── main.py               # CLI entry point & interactive menu
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
git clone https://github.com/mostafaahmedaly2003/student-grade-analyzer.git
cd student-grade-analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> Dependencies: `streamlit` and `pandas` for the dashboard, `colorama` for CLI colors (optional — the CLI works without it).

### 3a. Run the web dashboard

```bash
streamlit run dashboard.py
```

Opens automatically at `http://localhost:8501` in your browser.

### 3b. Run the CLI

```bash
python main.py
```

## Dashboard

The web dashboard includes:

- **KPI cards** — class average, median, GPA, pass/fail counts
- **Grade distribution bar chart** — students per letter grade
- **Pass vs Fail chart**
- **Interactive ranking table** — color-coded by grade
- **Live search** — filter students by name instantly
- **One-click export** — download JSON or CSV report

Load data by uploading a CSV or clicking **Load sample data** in the sidebar.

## CLI Usage

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
- streamlit, pandas (for the dashboard)
- colorama (optional, for CLI colors)

## License

MIT License — feel free to use, modify, and share.
