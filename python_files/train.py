import pandas as pd
import nltk
import re
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import pickle

# Load the NYT articles dataset
df = pd.read_csv("Datasets/nyt_articles.csv")

# Sample sentiment labeling: We'll assume that articles mentioning "good", "excellent" are positive
# and "bad", "worst" are negative (this is for demonstration; in a real case, we need labeled data)
positive_words = ["good", "excellent", "great", "amazing", "positive", "success"]
negative_words = ["bad", "worst", "terrible", "negative", "fail"]

def assign_sentiment(text):
    text = text.lower()
    if any(word in text for word in positive_words):
        return "positive"
    elif any(word in text for word in negative_words):
        return "negative"
    else:
        return "neutral"

df["sentiment"] = df["abstract"].astype(str).apply(assign_sentiment)

# Preprocessing function
def preprocess_text(text):
    text = text.lower()  
    text = re.sub(r'\W', ' ', text)  
    text = re.sub(r'\s+', ' ', text).strip()  
    text = " ".join([word for word in text.split() if word not in stopwords.words("english")])
    return text

df["cleaned_text"] = df["abstract"].astype(str).apply(preprocess_text)

# Feature extraction using TF-IDF
X = df["cleaned_text"]
y = df["sentiment"]

vectorizer = TfidfVectorizer(max_features=5000)
X_tfidf = vectorizer.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

# Train Logistic Regression Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model & vectorizer
with open("Artifacts/logistic_regression_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

with open("Artifacts/tfidf_vectorizer.pkl", "wb") as vec_file:
    pickle.dump(vectorizer, vec_file)

print("✅ Logistic Regression model trained and saved!")
