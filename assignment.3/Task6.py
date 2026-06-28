import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import (confusion_matrix, accuracy_score,
                             precision_score, recall_score,
                             f1_score, classification_report)

# --- Task 6: Handwritten Digit Recognition (SVM) ---
# Using sklearn built-in Digits dataset (8x8 images, 10 classes)

# 1. Load dataset
digits = load_digits()
X, y = digits.data, digits.target
print(f"Dataset shape: {X.shape}  Classes: {digits.target_names}")

# 2. Visualize sample images
fig, axes = plt.subplots(2, 5, figsize=(10, 4))
for ax, img, label in zip(axes.flat, digits.images, digits.target):
    ax.imshow(img, cmap="gray")
    ax.set_title(f"Label: {label}")
    ax.axis("off")
plt.suptitle("Sample Digit Images")
plt.tight_layout()
plt.savefig("task6_sample_images.png", dpi=150)
plt.show()

# 3. Normalize features to [0, 1]
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# 4. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42)

# 5. Train Linear SVM
svm_linear = SVC(kernel="linear", random_state=42)
svm_linear.fit(X_train, y_train)
y_pred_linear = svm_linear.predict(X_test)

# 6. Train RBF Kernel SVM
svm_rbf = SVC(kernel="rbf", random_state=42)
svm_rbf.fit(X_train, y_train)
y_pred_rbf = svm_rbf.predict(X_test)

# 7. Compare models
for name, y_pred in [("Linear SVM", y_pred_linear), ("RBF SVM", y_pred_rbf)]:
    print(f"\n=== {name} ===")
    print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred, average='weighted'):.4f}")
    print(f"Recall   : {recall_score(y_test, y_pred, average='weighted'):.4f}")
    print(f"F1-Score : {f1_score(y_test, y_pred, average='weighted'):.4f}")
    print(classification_report(y_test, y_pred))

# 8. Confusion matrices side by side
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
for ax, y_pred, title in zip(axes,
                              [y_pred_linear, y_pred_rbf],
                              ["Linear SVM", "RBF SVM"]):
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
    ax.set_title(f"Confusion Matrix — {title}")
    ax.set_xlabel("Predicted"); ax.set_ylabel("Actual")
plt.tight_layout()
plt.savefig("task6_confusion_matrices.png", dpi=150)
plt.show()
print("Saved: task6_confusion_matrices.png")

# 10. Kernel discussion
print("""
Kernel Effect:
- Linear SVM: finds a hyperplane in original feature space.
  Works well when data is linearly separable.
- RBF SVM: maps data to higher-dimensional space using
  Gaussian kernel, capturing non-linear patterns.
  Generally better for image/digit data with complex boundaries.
""")
