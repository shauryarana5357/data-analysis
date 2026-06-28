import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

# --- Task 1: House Price Prediction (Linear Regression) ---
# Dataset: train.csv from Kaggle House Prices competition

df = pd.read_csv(r"C:\Users\shaur.SHAURYA-NITRO\OneDrive\Videos\docs\study material\internship.nitj\python codes\assignment.3\train.csv")

# 1. First 10 records and info
print(df.head(10))
print(df.info())

# 2. Drop columns with >50% missing values
threshold = len(df) * 0.5
df.dropna(axis=1, thresh=int(threshold), inplace=True)

# 3. Fill missing values
for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

# 4. Encode categorical columns safely
le = LabelEncoder()
for col in df.select_dtypes(include="object").columns:
    df[col] = le.fit_transform(df[col].astype(str))

# 5. Features and target
X = df.drop(columns=["SalePrice", "Id"], errors="ignore")
y = df["SalePrice"]

# 6. Train/test split 80:20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Train Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# 8. Predict
y_pred = model.predict(X_test)

# 9. Metrics
mae  = mean_absolute_error(y_test, y_pred)
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)

print(f"\nMAE  : {mae:.2f}")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R2   : {r2:.4f}")

# 10. Actual vs Predicted plot
plt.figure(figsize=(8, 5))
plt.scatter(y_test, y_pred, alpha=0.5, color="steelblue", edgecolors="k", linewidths=0.3)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", lw=2, label="Perfect Fit")
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted House Prices")
plt.legend()
plt.tight_layout()
plt.savefig("task1_actual_vs_predicted.png", dpi=150)
plt.show()
print("Saved: task1_actual_vs_predicted.png")
