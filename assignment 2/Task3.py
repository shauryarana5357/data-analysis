import pandas as pd
import matplotlib.pyplot as plt

# --- Task 3: Healthcare Data Cleaning (Pandas Cleaning) ---
# Dataset: covid19_dataset.csv from Kaggle
# https://www.kaggle.com/datasets/imdevskp/corona-virus-report

# Load dataset
df = pd.read_csv("assignment 2\StudentsPerformance.csv")

print("=== Dataset Info ===")
df.info()
print("\n=== First 5 Rows ===")
print(df.head())

# Drop rows where 'age' or 'id' column is missing (only if those columns exist)
for col in ["age", "id"]:
    if col in df.columns:
        before = len(df)
        df.dropna(subset=[col], inplace=True)
        print(f"Dropped {before - len(df)} rows with missing '{col}'")
    else:
        print(f"Column '{col}' not found — skipping drop.")

print(f"\nRows after cleaning: {len(df)}")

# --- Plot 1: Active vs Recovered Cases ---
# Use country-wise or date-wise aggregated columns
active_col = next((c for c in df.columns if "active" in c.lower()), None)
recovered_col = next((c for c in df.columns if "recover" in c.lower()), None)

if active_col and recovered_col:
    # Aggregate by date or country (use first suitable grouping column)
    group_col = next((c for c in df.columns if "date" in c.lower() or "country" in c.lower()), None)

    if group_col:
        agg = df.groupby(group_col)[[active_col, recovered_col]].sum().reset_index()

        plt.figure(figsize=(12, 5))
        plt.plot(agg[group_col].astype(str), agg[active_col], label="Active Cases", color="orange")
        plt.plot(agg[group_col].astype(str), agg[recovered_col], label="Recovered Cases", color="green")
        plt.xticks(rotation=90, fontsize=6)
        plt.title("Active vs Recovered Cases")
        plt.xlabel(group_col)
        plt.ylabel("Count")
        plt.legend()
        plt.tight_layout()
        plt.savefig("task3_active_recovered.png", dpi=150)
        plt.show()
        print("Plot 1 saved: task3_active_recovered.png")
    else:
        print("No suitable grouping column found for Plot 1.")
else:
    print(f"Columns for active/recovered not found. Found: {list(df.columns)}")

# --- Plot 2: New Deaths vs New Cases ---
deaths_col = next((c for c in df.columns if "new_death" in c.lower() or "new death" in c.lower()), None)
cases_col  = next((c for c in df.columns if "new_case" in c.lower()  or "new case" in c.lower()), None)

if deaths_col and cases_col:
    group_col2 = next((c for c in df.columns if "date" in c.lower() or "country" in c.lower()), None)

    if group_col2:
        agg2 = df.groupby(group_col2)[[deaths_col, cases_col]].sum().reset_index()

        plt.figure(figsize=(12, 5))
        plt.plot(agg2[group_col2].astype(str), agg2[cases_col],  label="New Cases",  color="blue")
        plt.plot(agg2[group_col2].astype(str), agg2[deaths_col], label="New Deaths", color="red")
        plt.xticks(rotation=90, fontsize=6)
        plt.title("New Cases vs New Deaths")
        plt.xlabel(group_col2)
        plt.ylabel("Count")
        plt.legend()
        plt.tight_layout()
        plt.savefig("task3_new_cases_deaths.png", dpi=150)
        plt.show()
        print("Plot 2 saved: task3_new_cases_deaths.png")
    else:
        print("No suitable grouping column for Plot 2.")
else:
    print(f"Columns for new_cases/new_deaths not found. Found: {list(df.columns)}")
