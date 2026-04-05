import math
import json
import csv
import io

import streamlit as st
import pandas as pd

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="Student Grade Analyzer",
    page_icon="🎓",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Grade helpers (self-contained so dashboard has no CLI dependencies)
# ---------------------------------------------------------------------------

def get_letter_grade(score: float) -> str:
    if score >= 90: return "A"
    if score >= 80: return "B"
    if score >= 70: return "C"
    if score >= 60: return "D"
    return "F"

def get_gpa(score: float) -> float:
    if score >= 90: return 4.0
    if score >= 80: return 3.0
    if score >= 70: return 2.0
    if score >= 60: return 1.0
    return 0.0

def get_status(score: float) -> str:
    return "Pass" if score >= 60 else "Fail"

def build_df(students: list[dict]) -> pd.DataFrame:
    rows = []
    for s in students:
        grade = s["grade"]
        rows.append({
            "Name": s["name"],
            "Grade": grade,
            "Letter": get_letter_grade(grade),
            "GPA": get_gpa(grade),
            "Status": get_status(grade),
        })
    df = pd.DataFrame(rows)
    df = df.sort_values("Grade", ascending=False).reset_index(drop=True)
    df.index += 1
    return df

# ---------------------------------------------------------------------------
# Session state
# ---------------------------------------------------------------------------

if "students" not in st.session_state:
    st.session_state.students = []

# ---------------------------------------------------------------------------
# Sidebar — data input
# ---------------------------------------------------------------------------

with st.sidebar:
    st.title("🎓 Student Grade Analyzer")
    st.markdown("---")

    tab_upload, tab_manual = st.tabs(["Upload CSV", "Add Manually"])

    with tab_upload:
        st.markdown("**CSV format:** `name, grade`")
        uploaded = st.file_uploader("Choose a CSV file", type="csv", label_visibility="collapsed")
        if uploaded:
            try:
                content = uploaded.read().decode("utf-8")
                reader = csv.DictReader(io.StringIO(content))
                loaded = []
                for row in reader:
                    name = row.get("name", "").strip().title()
                    try:
                        grade = float(row.get("grade", ""))
                        if name and 0 <= grade <= 100:
                            loaded.append({"name": name, "grade": grade})
                    except ValueError:
                        pass
                if loaded:
                    st.session_state.students = loaded
                    st.success(f"Loaded {len(loaded)} students!")
                else:
                    st.error("No valid rows found in CSV.")
            except Exception as e:
                st.error(f"Error reading file: {e}")

        st.markdown("---")
        if st.button("Load sample data", use_container_width=True):
            st.session_state.students = [
                {"name": "Alice Johnson", "grade": 92},
                {"name": "Bob Smith", "grade": 75},
                {"name": "Carol Williams", "grade": 88},
                {"name": "David Brown", "grade": 62},
                {"name": "Emma Davis", "grade": 97},
                {"name": "Frank Miller", "grade": 45},
                {"name": "Grace Wilson", "grade": 78},
                {"name": "Henry Moore", "grade": 83},
                {"name": "Isabella Taylor", "grade": 91},
                {"name": "James Anderson", "grade": 55},
                {"name": "Karen Thomas", "grade": 69},
                {"name": "Liam Jackson", "grade": 84},
                {"name": "Mia White", "grade": 100},
                {"name": "Noah Harris", "grade": 73},
                {"name": "Olivia Martin", "grade": 58},
            ]
            st.success("Sample data loaded!")

    with tab_manual:
        with st.form("add_student", clear_on_submit=True):
            name = st.text_input("Student name")
            grade = st.number_input("Grade (0–100)", min_value=0.0, max_value=100.0, step=0.5)
            if st.form_submit_button("Add Student", use_container_width=True):
                if name.strip():
                    st.session_state.students.append({"name": name.strip().title(), "grade": grade})
                    st.success(f"Added {name.strip().title()}!")
                else:
                    st.error("Name cannot be empty.")

    st.markdown("---")
    if st.session_state.students:
        if st.button("Clear all students", use_container_width=True, type="secondary"):
            st.session_state.students = []
            st.rerun()

# ---------------------------------------------------------------------------
# Main content
# ---------------------------------------------------------------------------

students = st.session_state.students

if not students:
    st.title("🎓 Student Grade Analyzer")
    st.info("Add students using the sidebar to get started, or load the sample data.")
    st.stop()

df = build_df(students)
grades = df["Grade"].tolist()
total = len(grades)

# --- Stats calculations ---
avg = sum(grades) / total
sorted_grades = sorted(grades)
mid = total // 2
median = (sorted_grades[mid - 1] + sorted_grades[mid]) / 2 if total % 2 == 0 else sorted_grades[mid]
variance = sum((g - avg) ** 2 for g in grades) / total
std_dev = math.sqrt(variance)
class_gpa = sum(get_gpa(g) for g in grades) / total
pass_count = sum(1 for g in grades if g >= 60)
fail_count = total - pass_count
top = df.iloc[0]
lowest = df.iloc[-1]

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------

st.title("🎓 Student Grade Analyzer")
st.markdown(f"Analyzing **{total} student{'s' if total != 1 else ''}**")
st.markdown("---")

# ---------------------------------------------------------------------------
# KPI cards
# ---------------------------------------------------------------------------

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Class Average", f"{avg:.1f}")
c2.metric("Median Grade", f"{median:.1f}")
c3.metric("Class GPA", f"{class_gpa:.2f} / 4.0")
c4.metric("Passed", f"{pass_count} / {total}", f"{pass_count / total * 100:.0f}%")
c5.metric("Failed", f"{fail_count} / {total}", f"-{fail_count / total * 100:.0f}%", delta_color="inverse")

st.markdown("---")

# ---------------------------------------------------------------------------
# Charts row
# ---------------------------------------------------------------------------

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Grade Distribution")
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for g in grades:
        dist[get_letter_grade(g)] += 1
    dist_df = pd.DataFrame({"Letter Grade": list(dist.keys()), "Students": list(dist.values())})
    st.bar_chart(dist_df.set_index("Letter Grade"), color="#4f8bf9")

with col_right:
    st.subheader("Pass vs Fail")
    pf_df = pd.DataFrame({
        "Result": ["Pass", "Fail"],
        "Count": [pass_count, fail_count],
    })
    st.bar_chart(pf_df.set_index("Result"), color=["#22c55e"])

st.markdown("---")

# ---------------------------------------------------------------------------
# Student ranking table
# ---------------------------------------------------------------------------

st.subheader("Student Ranking")

def color_status(val):
    return "color: #22c55e; font-weight: bold" if val == "Pass" else "color: #ef4444; font-weight: bold"

def color_letter(val):
    palette = {"A": "#22c55e", "B": "#3b82f6", "C": "#f59e0b", "D": "#a855f7", "F": "#ef4444"}
    c = palette.get(val, "white")
    return f"color: {c}; font-weight: bold"

def color_grade(val):
    if val >= 80: return "color: #22c55e"
    if val >= 60: return "color: #f59e0b"
    return "color: #ef4444"

styled = (
    df.style
    .applymap(color_status, subset=["Status"])
    .applymap(color_letter, subset=["Letter"])
    .applymap(color_grade, subset=["Grade"])
    .format({"Grade": "{:.2f}", "GPA": "{:.1f}"})
)
st.dataframe(styled, use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------------------------
# Top & Lowest highlight
# ---------------------------------------------------------------------------

col_top, col_low = st.columns(2)
with col_top:
    st.success(f"**Top Student:** {top['Name']}  —  {top['Grade']:.2f} ({top['Letter']})")
with col_low:
    st.error(f"**Needs Support:** {lowest['Name']}  —  {lowest['Grade']:.2f} ({lowest['Letter']})")

st.markdown("---")

# ---------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------

st.subheader("Search Student")
query = st.text_input("Enter name (or partial name)", label_visibility="collapsed", placeholder="Search by name...")
if query:
    results = df[df["Name"].str.contains(query, case=False)]
    if results.empty:
        st.warning("No students found.")
    else:
        st.dataframe(results.style.format({"Grade": "{:.2f}", "GPA": "{:.1f}"}), use_container_width=True)

st.markdown("---")

# ---------------------------------------------------------------------------
# Export JSON
# ---------------------------------------------------------------------------

st.subheader("Export Report")
export_data = {
    "students": [
        {"name": row["Name"], "grade": row["Grade"], "letter": row["Letter"],
         "gpa": row["GPA"], "status": row["Status"]}
        for _, row in df.iterrows()
    ],
    "statistics": {
        "total": total, "average": round(avg, 2), "median": round(median, 2),
        "std_deviation": round(std_dev, 2), "class_gpa": round(class_gpa, 2),
        "passed": pass_count, "failed": fail_count,
        "pass_rate": round(pass_count / total * 100, 1),
    },
}
col_j, col_c, _ = st.columns([1, 1, 3])
col_j.download_button(
    "Download JSON",
    data=json.dumps(export_data, indent=2),
    file_name="report.json",
    mime="application/json",
    use_container_width=True,
)
csv_buf = io.StringIO()
df.to_csv(csv_buf, index_label="Rank")
col_c.download_button(
    "Download CSV",
    data=csv_buf.getvalue(),
    file_name="report.csv",
    mime="text/csv",
    use_container_width=True,
)
