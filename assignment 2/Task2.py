import pandas as pd

# --- Task 2: Student Records Management (Pandas) ---
# Dataset: StudentsPerformance.csv from Kaggle
# https://www.kaggle.com/datasets/spscientist/students-performance-in-exams

# Load dataset
df = pd.read_csv("assignment 2\StudentsPerformance.csv")

# Basic summary
print("=== Dataset Info ===")
df.info()

print("\n=== Statistical Summary ===")
print(df.describe())

# Preview
print("\n=== First 5 Rows ===")
print(df.head())

# Average math score grouped by gender
print("\n=== Avg Math Score by Gender ===")
gender_math = df.groupby("gender")["math score"].mean()
print(gender_math)

# Parental education level with highest average reading score
print("\n=== Avg Reading Score by Parental Education Level ===")
edu_reading = df.groupby("parental level of education")["reading score"].mean()
print(edu_reading)

best_edu = edu_reading.idxmax()
print(f"\nHighest avg reading score → Parental Education: '{best_edu}' ({edu_reading[best_edu]:.2f})")
