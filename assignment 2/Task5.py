import seaborn as sns
import matplotlib.pyplot as plt

# --- Task 5: Flower Classification Insights (Seaborn + Iris) ---

# Load built-in Iris dataset
iris = sns.load_dataset("iris")
print("=== Iris Dataset ===")
print(iris.head())
print(iris.describe())

# --- Plot 1: Pair Plot ---
pair = sns.pairplot(iris, hue="species", palette="Set2")
pair.fig.suptitle("Iris Pair Plot", y=1.02)
plt.savefig("task5_pairplot.png", dpi=150, bbox_inches="tight")
plt.show()

# --- Plot 2: Correlation Heatmap ---
plt.figure(figsize=(6, 5))
corr = iris.drop(columns="species").corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True)
plt.title("Correlation Heatmap of Iris Features")
plt.tight_layout()
plt.savefig("task5_heatmap.png", dpi=150)
plt.show()

# --- Plot 3: Boxplot — Petal Length per Species ---
plt.figure(figsize=(7, 5))
sns.boxplot(data=iris, x="species", y="petal_length", palette="Set3")
plt.title("Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.savefig("task5_boxplot_petal_length.png", dpi=150)
plt.show()

# --- Insights ---
print("""
=== Insights ===
1. Petal length and petal width are highly correlated (r ≈ 0.96).
   Virginica has the largest petals; Setosa has the smallest.
2. Setosa is clearly separable from the other two species
   across all features, making it easy to classify visually.
""")
