import os

print("Working directory:", os.getcwd())
print("Files in this folder:", os.listdir(os.getcwd()))



import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- Task 4: Sales Performance Dashboard (Matplotlib) ---
# Dataset: sales_data.csv (Retail Sales Dataset from Kaggle)

# Load dataset
df = pd.read_csv("sales_data.csv")
print("Columns:", df.columns.tolist())
print(df.head())

# --- Identify key columns (flexible for common Kaggle retail datasets) ---
# Adjust column names below if your CSV uses different names
date_col     = next((c for c in df.columns if "date" in c.lower()), None)
qty_col      = next((c for c in df.columns if "quant" in c.lower()), None)
price_col    = next((c for c in df.columns if "price" in c.lower() or "unit" in c.lower()), None)
revenue_col  = next((c for c in df.columns if "revenue" in c.lower() or "sales" in c.lower() or "amount" in c.lower()), None)
product_col  = next((c for c in df.columns if "product" in c.lower() or "category" in c.lower()), None)

# --- Compute Revenue if not present ---
if revenue_col is None and qty_col and price_col:
    df["Revenue"] = df[qty_col] * df[price_col]
    revenue_col = "Revenue"

# --- Plot 1: Monthly Revenue Trend (Line Graph) ---
if date_col and revenue_col:
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df["Month"] = df[date_col].dt.to_period("M")
    monthly = df.groupby("Month")[revenue_col].sum()

    plt.figure(figsize=(10, 4))
    plt.plot(monthly.index.astype(str), monthly.values, marker="o", color="steelblue")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("task4_monthly_revenue.png", dpi=150)
    plt.show()
else:
    # Generate synthetic monthly revenue if columns missing
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    revenue = np.random.randint(50000, 200000, 12)
    plt.figure(figsize=(10, 4))
    plt.plot(months, revenue, marker="o", color="steelblue")
    plt.title("Monthly Revenue Trend (Synthetic)")
    plt.xlabel("Month"); plt.ylabel("Revenue")
    plt.grid(True); plt.tight_layout()
    plt.savefig("task4_monthly_revenue.png", dpi=150)
    plt.show()

# --- Plot 2: Bar Chart — Revenue by Product Category (Clothing vs Electronics) ---
if product_col and revenue_col:
    cat_rev = df.groupby(product_col)[revenue_col].sum()
    # Filter for clothing and electronics if present
    targets = [c for c in cat_rev.index if any(k in str(c).lower() for k in ["cloth", "electron"])]
    if targets:
        cat_rev = cat_rev[targets]

    plt.figure(figsize=(7, 4))
    plt.bar(cat_rev.index.astype(str), cat_rev.values, color=["tomato", "royalblue"])
    plt.title("Revenue by Product Category")
    plt.xlabel("Category"); plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("task4_revenue_by_category.png", dpi=150)
    plt.show()
else:
    # Synthetic bar chart
    categories = ["Clothing", "Electronics"]
    rev = [120000, 180000]
    plt.figure(figsize=(6, 4))
    plt.bar(categories, rev, color=["tomato", "royalblue"])
    plt.title("Revenue: Clothing vs Electronics (Synthetic)")
    plt.xlabel("Category"); plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("task4_revenue_by_category.png", dpi=150)
    plt.show()

# --- Plot 3: Histogram — Distribution of Quantity Ordered ---
if qty_col:
    plt.figure(figsize=(7, 4))
    plt.hist(df[qty_col].dropna(), bins=20, color="mediumseagreen", edgecolor="black")
    plt.title("Distribution of Quantity Ordered")
    plt.xlabel("Quantity"); plt.ylabel("Frequency")
    plt.grid(True); plt.tight_layout()
    plt.savefig("task4_qty_histogram.png", dpi=150)
    plt.show()
else:
    qty = np.random.randint(1, 20, 500)
    plt.figure(figsize=(7, 4))
    plt.hist(qty, bins=20, color="mediumseagreen", edgecolor="black")
    plt.title("Distribution of Quantity Ordered (Synthetic)")
    plt.xlabel("Quantity"); plt.ylabel("Frequency")
    plt.grid(True); plt.tight_layout()
    plt.savefig("task4_qty_histogram.png", dpi=150)
    plt.show()

# --- Plot 4: Scatter — Unit Price vs Revenue ---
if price_col and revenue_col:
    plt.figure(figsize=(7, 4))
    plt.scatter(df[price_col], df[revenue_col], alpha=0.4, color="purple")
    plt.title("Unit Price vs Revenue")
    plt.xlabel("Unit Price"); plt.ylabel("Revenue")
    plt.grid(True); plt.tight_layout()
    plt.savefig("task4_price_vs_revenue.png", dpi=150)
    plt.show()
else:
    prices  = np.random.uniform(5, 500, 300)
    rev_s   = prices * np.random.randint(1, 15, 300)
    plt.figure(figsize=(7, 4))
    plt.scatter(prices, rev_s, alpha=0.4, color="purple")
    plt.title("Unit Price vs Revenue (Synthetic)")
    plt.xlabel("Unit Price"); plt.ylabel("Revenue")
    plt.grid(True); plt.tight_layout()
    plt.savefig("task4_price_vs_revenue.png", dpi=150)
    plt.show()

print("All Task 4 plots saved.")
