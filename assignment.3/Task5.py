import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# --- Task 5: Survival Prediction (Random Forest) ---
# Dataset: train.csv from Kaggle Titanic competition

df = pd.read_csv("titanic_train.csv")   # rename to titanic_train.csv if needed
print(df.head())
print(df.info())

# 2. Preprocessing
# Drop low-utility columns
df.drop(columns=["Name", "Ticket", "Cabin", "PassengerId"], errors="ignore", inplace=True)

# Fill missing Age with median, Embarked with mode
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Fare"].fillna(df["Fare"].median(), inplace=True)
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

# Encode categorical
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

X = df.drop(columns=["Survived"])
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# 3. Decision Tree
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
dt_train_acc = accuracy_score(y_train, dt.predict(X_train))
dt_test_acc  = accuracy_score(y_test,  dt.predict(X_test))

# 4. Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_train_acc = accuracy_score(y_train, rf.predict(X_train))
rf_test_acc  = accuracy_score(y_test,  rf.predict(X_test))

# 5. Compare accuracies
print(f"\nDecision Tree  — Train: {dt_train_acc:.4f}  Test: {dt_test_acc:.4f}")
print(f"Random Forest  — Train: {rf_train_acc:.4f}  Test: {rf_test_acc:.4f}")

# 6. Classification reports
print("\n--- Decision Tree Report ---")
print(classification_report(y_test, dt.predict(X_test)))
print("--- Random Forest Report ---")
print(classification_report(y_test, rf.predict(X_test)))

# 7 & 8. Feature importance
feat_imp = pd.Series(rf.feature_importances_, index=X.columns).sort_values()

plt.figure(figsize=(7, 5))
feat_imp.plot(kind="barh", color="coral")
plt.title("Random Forest — Feature Importance (Titanic)")
plt.xlabel("Importance Score")
plt.tight_layout()
plt.savefig("task5_feature_importance.png", dpi=150)
plt.show()
print("Saved: task5_feature_importance.png")

# 9 & 10. Analysis
print(f"""
Ensemble Learning Benefits:
- Decision Tree: prone to overfitting (train={dt_train_acc:.2f} vs test={dt_test_acc:.2f}).
- Random Forest aggregates {rf.n_estimators} trees, reducing variance via bagging.
- Result: higher and more stable test accuracy ({rf_test_acc:.2f}).
- Feature importance shows Age, Fare, and Sex are top predictors of survival.
""")
