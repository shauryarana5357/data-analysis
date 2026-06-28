import numpy as np
import matplotlib.pyplot as plt

# --- Task 8: Histogram Analysis ---

np.random.seed(0)
# 200 normally distributed exam scores (mean=75, std=10)
scores = np.random.normal(loc=75, scale=10, size=200)

# --- a & b & c) Histogram with 15 bins, styled, labeled ---
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Plot 1: Count histogram
axes[0].hist(scores, bins=15, color='steelblue', edgecolor='black', alpha=0.85)
axes[0].set_title('Exam Score Distribution (Count)')
axes[0].set_xlabel('Score')
axes[0].set_ylabel('Frequency')
axes[0].grid(True, linestyle='--', alpha=0.6)

# --- d) Second histogram with density=True, overlaid with transparency ---
axes[1].hist(scores, bins=15, color='steelblue', edgecolor='black',
             alpha=0.5, label='Count')
axes[1].hist(scores, bins=15, color='tomato', edgecolor='black',
             alpha=0.5, density=True, label='Density')
axes[1].set_title('Overlaid Histograms (Count + Density)')
axes[1].set_xlabel('Score')
axes[1].set_ylabel('Frequency / Density')
axes[1].legend()
axes[1].grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.savefig("task8_histograms.png", dpi=150)
plt.show()
print("Saved: task8_histograms.png")
