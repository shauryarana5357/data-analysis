import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import pandas as pd

# --- Task 3: Flower Species Classification (KNN) ---

# 1. Load Iris dataset
iris = load_iris()
X, y = iris.data, iris.target
df = pd.DataFrame(X, columns=iris.feature_names)
df["species"] = [iris.target_names[i] for i in y]

# 2. Exploratory Data Analysis
print(df.head())
print(df.describe())
print(df["species"].value_counts())

# 3. Pair plot visualization
pair = sns.pairplot(df, hue="species", palette="Set2")
pair.fig.suptitle("Iris Feature Pair Plot", y=1.02)
plt.savefig("task3_pairplot.png", dpi=150, bbox_inches="tight")
plt.show()

# 4. Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42)

# 5 & 6. Train KNN for K = 1 to 15 and record accuracies
accuracies = []
for k in range(1, 16):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    accuracies.append(knn.score(X_test, y_test))
    print(f"K={k:2d}  Accuracy={accuracies[-1]:.4f}")

# 7. Best K
best_k = accuracies.index(max(accuracies)) + 1
print(f"\nBest K = {best_k}  (Accuracy = {max(accuracies):.4f})")

# 8. Predictions with best model
best_knn = KNeighborsClassifier(n_neighbors=best_k)
best_knn.fit(X_train, y_train)
y_pred = best_knn.predict(X_test)
print("\nClassification Report:\n", classification_report(
    y_test, y_pred, target_names=iris.target_names))

# 9. K vs Accuracy plot
plt.figure(figsize=(8, 4))
plt.plot(range(1, 16), accuracies, marker="o", color="teal")
plt.axvline(best_k, color="red", linestyle="--", label=f"Best K={best_k}")
plt.xlabel("K (Number of Neighbors)")
plt.ylabel("Test Accuracy")
plt.title("K vs Accuracy — KNN on Iris Dataset")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("task3_k_vs_accuracy.png", dpi=150)
plt.show()
print("Saved: task3_k_vs_accuracy.png")

# 10. Analysis
print("""
K Effect Analysis:
- K=1: Overfits — sensitive to noise, high variance.
- Small K: Low bias, high variance (complex boundaries).
- Large K: High bias, low variance (smoother boundaries, may underfit).
- Optimal K balances bias-variance tradeoff.
""")