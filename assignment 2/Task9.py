import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

np.random.seed(7)

# --- Synthetic Data ---
study_hours       = np.random.uniform(1, 10, 60)
exam_scores       = 50 + 4.5 * study_hours + np.random.normal(0, 5, 60)
assignment_scores = 40 + 5.2 * study_hours + np.random.normal(0, 6, 60)

# ============================================================
# PART 1 — Scatter Plots
# ============================================================

fig, ax = plt.subplots(figsize=(8, 5))

# a) Study hours vs Exam scores
ax.scatter(study_hours, exam_scores,
           color='royalblue', marker='o', alpha=0.7, label='Exam Scores')

# b) Study hours vs Assignment scores (different color & marker)
ax.scatter(study_hours, assignment_scores,
           color='tomato', marker='^', alpha=0.7, label='Assignment Scores')

# c) Labels, title, legend, grid
ax.set_xlabel('Study Hours')
ax.set_ylabel('Score')
ax.set_title('Study Hours vs Exam & Assignment Scores')
ax.legend()
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()

# d) Correlation comment
corr_exam = np.corrcoef(study_hours, exam_scores)[0, 1]
corr_asn  = np.corrcoef(study_hours, assignment_scores)[0, 1]
print(f"Correlation — Study Hours vs Exam Scores      : {corr_exam:.3f}")
print(f"Correlation — Study Hours vs Assignment Scores: {corr_asn:.3f}")
print("""
Observation:
Both exam and assignment scores show strong positive correlation
with study hours (~0.85+). More study hours → higher scores.
Assignment scores have a slightly steeper slope, suggesting
consistent practice matters more for assignments than exams.
""")

# ============================================================
# PART 2 — Save in multiple formats & resolutions
# ============================================================

# PNG
fig.savefig("task9_scatter.png")
print("Saved: task9_scatter.png")

# PDF
fig.savefig("task9_scatter.pdf")
print("Saved: task9_scatter.pdf")

# SVG
fig.savefig("task9_scatter.svg")
print("Saved: task9_scatter.svg")

# High-resolution PNG (300 DPI)
fig.savefig("task9_scatter_hires.png", dpi=300)
print("Saved: task9_scatter_hires.png (300 DPI)")

plt.close()

# --- Individual plots saved separately ---
# Exam score scatter
fig1, a1 = plt.subplots()
a1.scatter(study_hours, exam_scores, color='royalblue', marker='o', alpha=0.7)
a1.set(xlabel='Study Hours', ylabel='Exam Score', title='Study Hours vs Exam Scores')
a1.grid(True, linestyle='--', alpha=0.5)
fig1.savefig("task9_scatter_exam_scores.png", dpi=150)
plt.close(fig1)

# Assignment score scatter
fig2, a2 = plt.subplots()
a2.scatter(study_hours, assignment_scores, color='tomato', marker='^', alpha=0.7)
a2.set(xlabel='Study Hours', ylabel='Assignment Score', title='Study Hours vs Assignment Scores')
a2.grid(True, linestyle='--', alpha=0.5)
fig2.savefig("task9_scatter_assignment_scores.png", dpi=150)
plt.close(fig2)


# ============================================================
# Function: auto-generate and save chart by type
# ============================================================

def generate_and_save(data, chart_type, filename, title="Chart", xlabel="X", ylabel="Y"):
    """
    data      : dict with keys based on chart_type
    chart_type: 'line' | 'bar' | 'scatter' | 'hist' | 'pie'
    filename  : output file path (e.g. 'output.png')
    """
    fig, ax = plt.subplots(figsize=(7, 4))

    if chart_type == 'line':
        ax.plot(data['x'], data['y'], marker='o', color='steelblue')
    elif chart_type == 'bar':
        ax.bar(data['x'], data['y'], color='mediumseagreen')
    elif chart_type == 'scatter':
        ax.scatter(data['x'], data['y'], alpha=0.6, color='purple')
    elif chart_type == 'hist':
        ax.hist(data['values'], bins=data.get('bins', 10), color='coral', edgecolor='black')
    elif chart_type == 'pie':
        ax.pie(data['values'], labels=data['labels'], autopct='%1.1f%%')
    else:
        raise ValueError(f"Unsupported chart_type: {chart_type}")

    ax.set_title(title)
    if chart_type not in ('pie',):
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    fig.savefig(filename, dpi=150)
    plt.close(fig)
    print(f"Saved: {filename}")


# Example usage of the function
generate_and_save({'x': study_hours, 'y': exam_scores},
                  chart_type='scatter',
                  filename='task9_auto_scatter.png',
                  title='Auto-Generated Scatter',
                  xlabel='Study Hours',
                  ylabel='Exam Score')


# ============================================================
# SUBPLOT DASHBOARD (2×2 Grid)
# ============================================================

months       = ['Q1', 'Q2', 'Q3', 'Q4']
sales        = [100000, 150000, 120000, 180000]
departments  = ['IT', 'HR', 'Finance', 'Marketing']
performance  = [85, 78, 92, 88]
companies    = ['Company A', 'Company B', 'Company C', 'Others']
market_share = [35, 25, 20, 20]
ages         = [25, 28, 32, 29, 35, 31, 27, 33, 30, 36, 28, 29, 31, 34, 26]

fig, axes = plt.subplots(2, 2, figsize=(13, 9))

# a) Top-left: Line graph — Monthly Sales
axes[0, 0].plot(months, sales, marker='s', color='steelblue', linewidth=2)
axes[0, 0].set_title('Quarterly Sales Data')
axes[0, 0].set_xlabel('Quarter')
axes[0, 0].set_ylabel('Sales (₹)')
axes[0, 0].grid(True, linestyle='--', alpha=0.5)

# b) Top-right: Bar chart — Department Performance
bar_colors = ['#4CAF50', '#FF9800', '#2196F3', '#E91E63']
axes[0, 1].bar(departments, performance, color=bar_colors)
axes[0, 1].set_title('Department Performance')
axes[0, 1].set_xlabel('Department')
axes[0, 1].set_ylabel('Performance Score')
axes[0, 1].set_ylim(0, 110)
axes[0, 1].grid(True, linestyle='--', alpha=0.5, axis='y')

# c) Bottom-left: Pie chart — Market Share
pie_colors  = ['#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0']
explode_pie = (0.05, 0.05, 0.05, 0.05)
axes[1, 0].pie(market_share, labels=companies, autopct='%1.1f%%',
               colors=pie_colors, explode=explode_pie, startangle=90)
axes[1, 0].set_title('Market Share Distribution')

# d) Bottom-right: Histogram — Employee Age Distribution
axes[1, 1].hist(ages, bins=6, color='mediumpurple', edgecolor='black', alpha=0.85)
axes[1, 1].set_title('Employee Age Distribution')
axes[1, 1].set_xlabel('Age')
axes[1, 1].set_ylabel('Count')
axes[1, 1].grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig("task9_dashboard.png", dpi=150)
plt.show()
print("Saved: task9_dashboard.png")
