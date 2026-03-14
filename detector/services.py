import joblib
import re


model, vectorizer = joblib.load("model/scam_model.pkl")


keywords = [
    "crypto investment", "guaranteed profit", "send money", "urgent transfer"
]

def keyword_score(text):
    score = 0
    for word in keywords:
        if word in text.lower():
            score += 1
    return min(score * 0.25, 1)  

def url_score(text):
    urls = re.findall(r'https?://\S+', text)
    return 0.5 if urls else 0

def detect_scam(text):
    vec = vectorizer.transform([text])
    ml_prob = model.predict_proba(vec)[0][1]

    k_score = keyword_score(text)
    u_score = url_score(text)

    final_score = 0.7 * ml_prob + 0.2 * k_score + 0.1 * u_score

    percent_score = round(final_score * 100)

    return {
        "scam_probability": percent_score,  
        "label": "scam" if final_score > 0.5 else "not_scam"
    }