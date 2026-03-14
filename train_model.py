import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("data/scam_dataset.csv")

df['text'] = df['text'].str.lower().str.replace(r"[^a-z0-9\s]", "", regex=True)

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