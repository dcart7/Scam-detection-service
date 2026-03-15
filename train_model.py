import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# Source directly from the project dataset (class,message,...)
df = pd.read_csv(
    "Scam-detection-service/scam.csv",
    usecols=[0, 1],
    header=0,
    names=["label", "text"],
    encoding_errors="replace",
    engine="python",
)

df = df.dropna(subset=["label", "text"])
df["label"] = df["label"].astype(str).str.strip().str.lower()
# Binary target: ham vs scam (spam/smishing/etc.)
df["label"] = df["label"].apply(lambda v: "ham" if v == "ham" else "scam")
df["text"] = df["text"].astype(str).str.lower().str.replace(r"[^a-z0-9\s]", "", regex=True)

X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

model = LogisticRegression()
model.fit(X_train_vec, y_train)

print("Accuracy:", model.score(X_test_vec, y_test))

import os
os.makedirs("model", exist_ok=True)
joblib.dump((model, vectorizer), "model/scam_model.pkl")
