import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (confusion_matrix, accuracy_score,
                             precision_score, recall_score, f1_score,
                             classification_report)

# --- Task 2: Tumor Classification (Logistic Regression) ---
# Dataset: Breast Cancer Wisconsin (built-in sklearn)

data = load_breast_cancer()
X, y = data.data, data.target

# 2. Dataset info
print("Shape     :", X.shape)
print("Features  :", data.feature_names)
print("Classes   :", data.target_names)   # 0=malignant, 1=benign

# 3. Feature scaling — important for Logistic Regression
#    Without scaling, features with large ranges dominate gradient descent
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42)

# 5. Train Logistic Regression
model = LogisticRegression(max_iter=10000, random_state=42)
model.fit(X_train, y_train)

# 6. Predict
y_pred = model.predict(X_test)

# 7 & 8. Metrics
print("\nAccuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall   :", recall_score(y_test, y_pred))
print("F1-Score :", f1_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(
    y_test, y_pred, target_names=data.target_names))

# 9. Confusion matrix plot
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=data.target_names,
            yticklabels=data.target_names)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix — Tumor Classification")
plt.tight_layout()
plt.savefig("task2_confusion_matrix.png", dpi=150)
plt.show()
print("Saved: task2_confusion_matrix.png")

# 10. Importance of feature scaling
print("""
Feature Scaling Importance:
- Logistic Regression uses gradient-based optimization.
- Features with large magnitudes dominate updates, causing slow convergence.
- StandardScaler (mean=0, std=1) ensures equal contribution from all features,
  leading to faster convergence and better accuracy.
""")