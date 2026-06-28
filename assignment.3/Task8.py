import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings("ignore")

# --- Task 8: Customer Segmentation (K-Means Clustering) ---
# Dataset: Mall_Customers.csv from Kaggle

df = pd.read_csv(r"C:\Users\shaur.SHAURYA-NITRO\OneDrive\Videos\docs\study material\internship.nitj\python codes\assignment.3\Mall_Customers.csv")
print(df.head())
print(df.info())

# 2. Visualize feature distributions
df.hist(figsize=(10, 6), color="steelblue", edgecolor="black")
plt.suptitle("Feature Distributions")
plt.tight_layout()
plt.savefig("task8_distributions.png", dpi=150)
plt.show()

# 3. Select relevant features: Annual Income & Spending Score
X = df[["Annual Income (k$)", "Spending Score (1-100)"]].values

# 4. Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 5 & 6. Elbow Curve — inertia for K=1 to 10
inertias = []
K_range = range(1, 11)
for k in K_range:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)

plt.figure(figsize=(7, 4))
plt.plot(K_range, inertias, marker="o", color="teal")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia (WCSS)")
plt.title("Elbow Curve — Optimal K")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("task8_elbow_curve.png", dpi=150)
plt.show()

# 7. Optimal K (elbow point — typically K=5 for this dataset)
optimal_k = 5
print(f"Optimal K chosen: {optimal_k}")

# 8. Train final K-Means model
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# 9. Visualize clusters
plt.figure(figsize=(8, 6))
palette = sns.color_palette("Set2", optimal_k)
sns.scatterplot(data=df,
                x="Annual Income (k$)",
                y="Spending Score (1-100)",
                hue="Cluster",
                palette=palette,
                s=80, edgecolor="black", linewidth=0.4)

# Plot centroids (inverse-transform to original scale)
centers = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centers[:, 0], centers[:, 1],
            s=200, c="red", marker="X", zorder=5, label="Centroids")
plt.title(f"Customer Segments (K={optimal_k})")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.tight_layout()
plt.savefig("task8_clusters.png", dpi=150)
plt.show()
print("Saved: task8_elbow_curve.png, task8_clusters.png")

# 10. Cluster interpretation
print("\n=== Cluster Characteristics ===")
summary = df.groupby("Cluster")[["Annual Income (k$)", "Spending Score (1-100)"]].mean()
print(summary)

print("""
Cluster Interpretation (typical for Mall Customers):
  Cluster 0 — Low Income, Low Spending  : Budget-conscious customers
  Cluster 1 — High Income, Low Spending : Careful/wealthy savers
  Cluster 2 — Average Income, Average Spending: Regular shoppers
  Cluster 3 — Low Income, High Spending : Impulsive buyers
  Cluster 4 — High Income, High Spending: Premium target customers
(Actual labels depend on your run — check summary above.)
""")
