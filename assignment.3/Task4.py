import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# --- Task 4: Customer Purchase Prediction (Decision Tree) ---
# Dataset: Social_Network_Ads.csv from Kaggle

df = pd.read_csv("Social_Network_Ads.csv")

# 2. Summary statistics
print(df.head())
print(df.describe())
print(df.info())

# 3. Encode categorical variables (e.g., Gender)
le = LabelEncoder()
for col in df.select_dtypes(include="object").columns:
    df[col] = le.fit_transform(df[col])

# Features and target
X = df.drop(columns=["Purchased", "User ID"], errors="ignore")
y = df["Purchased"]

# 4. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# 5 & 6. Train Decision Trees with different depths
depths = [3, 5, 10, None]
results = {}

for d in depths:
    clf = DecisionTreeClassifier(max_depth=d, random_state=42)
    clf.fit(X_train, y_train)
    acc = accuracy_score(y_test, clf.predict(X_test))
    results[str(d)] = {"model": clf, "accuracy": acc}
    print(f"Depth={str(d):4s}  Accuracy={acc:.4f}")

# 7. Best tree (highest accuracy)
best_depth = max(results, key=lambda d: results[d]["accuracy"])
best_model = results[best_depth]["model"]
print(f"\nBest Depth: {best_depth}  Accuracy: {results[best_depth]['accuracy']:.4f}")

# Visualize best Decision Tree (cap display depth for readability)
plt.figure(figsize=(20, 8))
plot_tree(best_model, feature_names=X.columns.tolist(),
          class_names=["Not Buy", "Buy"],
          filled=True, max_depth=3, fontsize=9)
plt.title(f"Decision Tree (depth={best_depth}, shown up to 3 levels)")
plt.tight_layout()
plt.savefig("task4_decision_tree.png", dpi=150)
plt.show()

# 8. Confusion matrix and classification report for best model
y_pred = best_model.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Greens",
            xticklabels=["Not Buy", "Buy"],
            yticklabels=["Not Buy", "Buy"])
plt.xlabel("Predicted"); plt.ylabel("Actual")
plt.title("Confusion Matrix — Decision Tree")
plt.tight_layout()
plt.savefig("task4_confusion_matrix.png", dpi=150)
plt.show()

print("\nClassification Report:\n",
      classification_report(y_test, y_pred, target_names=["Not Buy", "Buy"]))

# 9. Feature importance
importances = pd.Series(best_model.feature_importances_, index=X.columns)
importances.sort_values().plot(kind="barh", color="steelblue",
                                title="Feature Importances")
plt.tight_layout()
plt.savefig("task4_feature_importance.png", dpi=150)
plt.show()
print("Saved: task4_decision_tree.png, task4_confusion_matrix.png, task4_feature_importance.png")
