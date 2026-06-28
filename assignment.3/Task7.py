import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import (confusion_matrix, accuracy_score,
                             precision_score, recall_score,
                             f1_score, classification_report)
import numpy as np

# --- Task 7: Email Spam Detection (Naive Bayes) ---
# Dataset: spam.csv from Kaggle SMS Spam Collection

df = pd.read_csv(r"C:\Users\shaur.SHAURYA-NITRO\OneDrive\Videos\docs\study material\internship.nitj\python codes\assignment.3\spam.csv", encoding="latin-1")[["v1", "v2"]]
df.columns = ["label", "message"]

# 2. Class distribution
print("Class Distribution:\n", df["label"].value_counts())
df["label"].value_counts().plot(kind="bar", color=["steelblue", "tomato"])
plt.title("Spam vs Ham Distribution")
plt.xlabel("Class"); plt.ylabel("Count")
plt.tight_layout()
plt.savefig("task7_class_distribution.png", dpi=150)
plt.show()

# Encode labels: ham=0, spam=1
df["label_enc"] = df["label"].map({"ham": 0, "spam": 1})

# 3. TF-IDF vectorization
tfidf = TfidfVectorizer(stop_words="english", max_features=5000)
X = tfidf.fit_transform(df["message"])
y = df["label_enc"]

# 4. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# 5. Train Multinomial Naive Bayes
model = MultinomialNB()
model.fit(X_train, y_train)

# 6. Predict
y_pred = model.predict(X_test)

# 7 & 8. Confusion matrix and metrics
cm = confusion_matrix(y_test, y_pred)
print(f"\nAccuracy : {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f}")
print(f"Recall   : {recall_score(y_test, y_pred):.4f}")
print(f"F1-Score : {f1_score(y_test, y_pred):.4f}")
print("\nClassification Report:\n",
      classification_report(y_test, y_pred, target_names=["Ham", "Spam"]))

plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Oranges",
            xticklabels=["Ham", "Spam"],
            yticklabels=["Ham", "Spam"])
plt.xlabel("Predicted"); plt.ylabel("Actual")
plt.title("Confusion Matrix — Spam Detection")
plt.tight_layout()
plt.savefig("task7_confusion_matrix.png", dpi=150)
plt.show()

# 9. Top predictive words for SPAM
feature_names = tfidf.get_feature_names_out()
spam_idx = 1   # class index for spam
top_n = 15
top_spam_words = np.argsort(model.feature_log_prob_[spam_idx])[-top_n:][::-1]

print(f"\nTop {top_n} words predicting SPAM:")
for i in top_spam_words:
    print(f"  {feature_names[i]}")

# Bar chart of top spam words
plt.figure(figsize=(8, 5))
word_scores = model.feature_log_prob_[spam_idx][top_spam_words]
plt.barh([feature_names[i] for i in top_spam_words][::-1],
         word_scores[::-1], color="tomato")
plt.xlabel("Log Probability")
plt.title("Top 15 Spam-Predictive Words")
plt.tight_layout()
plt.savefig("task7_top_spam_words.png", dpi=150)
plt.show()
print("Saved: task7_confusion_matrix.png, task7_top_spam_words.png")

# 10. Strengths of Naive Bayes for text
print("""
Naive Bayes Strengths for Text Classification:
- Fast training: closed-form probability estimates, no iterations.
- Works well with high-dimensional sparse data (TF-IDF vectors).
- Performs well even with small training datasets.
- The 'naive' independence assumption rarely hurts in text tasks.
- Naturally handles multi-class problems.
""")
