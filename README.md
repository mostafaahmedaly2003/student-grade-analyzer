# Student Grade Analyzer

A modular Python tool for analyzing academic performance metrics — supports grade distribution analysis, per-student reporting, and visual dashboards.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## Features

- Grade distribution analysis across subjects and cohorts
- Per-student performance breakdown with trend tracking
- Visual dashboard with charts and statistics (`dashboard.py`)
- Exportable PDF/CSV reports (`reports.py`)
- Formatted terminal output (`display.py`)
- Modular architecture — each component is independently usable

---

## Project Structure

```
student-grade-analyzer/
├── main.py              # Entry point — runs the full pipeline
├── analyzer.py          # Core analysis logic
├── dashboard.py         # Visual dashboard (charts & graphs)
├── reports.py           # Report generation (PDF/CSV export)
├── display.py           # Terminal output formatting
├── student.py           # Student data model
├── test.py              # Unit tests
├── sample_students.csv  # Sample dataset for testing
└── requirements.txt     # Dependencies
```

---

## Installation

```bash
git clone https://github.com/mostafaahmedaly2003/student-grade-analyzer.git
cd student-grade-analyzer
pip install -r requirements.txt
```

---

## Usage

```bash
# Run full analysis pipeline on sample data
python main.py

# Run with your own CSV file
python main.py --input your_students.csv

# Launch the visual dashboard
python dashboard.py

# Run tests
python test.py
```

---

## Input Format

The tool expects a CSV file with the following columns:

```csv
student_id,name,subject,grade,semester
001,Ahmed Mohamed,Math,88,Fall2025
001,Ahmed Mohamed,Physics,74,Fall2025
002,Sara Ali,Math,92,Fall2025
```

---

## Sample Output

```
=== Grade Analysis Report ===
Total Students : 30
Average Grade  : 78.4
Highest Grade  : 98 (Ahmed Mohamed — Math)
Lowest Grade   : 42 (...)
Pass Rate      : 86.7%

Grade Distribution:
  A (90-100): ████████  8 students
  B (80-89) : ████████████  12 students
  C (70-79) : ██████  6 students
  D (60-69) : ██  2 students
  F (<60)   : ██  2 students
```

---

## Tech Stack

- **Python 3.8+**
- pandas — data processing
- matplotlib / seaborn — visualization
- reportlab or fpdf — PDF export

---

## Use Cases

- Teaching assistants tracking student performance
- Instructors generating end-of-semester reports
- Academic departments analyzing grade trends

---

## Author

**Mostafa Ahmed** — AI/ML Engineer & Teaching Assistant @MUST  
[LinkedIn](https://www.linkedin.com/in/mostafa-ahmed-ai/) · [GitHub](https://github.com/mostafaahmedaly2003)
