import pickle
import pandas as pd
import re
from nltk.corpus import stopwords


# Preprocessing function
def preprocess_text(text):
    text = text.lower()  
    text = re.sub(r'\W', ' ', text)  
    text = re.sub(r'\s+', ' ', text).strip()  
    text = " ".join([word for word in text.split() if word not in stopwords.words("english")])
    return text

# Load saved model & vectorizer
with open("Artifacts/logistic_regression_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("Artifacts/tfidf_vectorizer.pkl", "rb") as vec_file:
    vectorizer = pickle.load(vec_file)

# Load new NYT articles
df_new = pd.read_csv("Datasets/nyt_articles.csv")

# Preprocess text
df_new["cleaned_text"] = df_new["abstract"].astype(str).apply(preprocess_text)

# Convert to numerical features
X_new_tfidf = vectorizer.transform(df_new["cleaned_text"])

# Predict sentiment
df_new["predicted_sentiment"] = model.predict(X_new_tfidf)

# Save updated dataset
df_new.to_csv("Datasets/nyt_articles_with_sentiment.csv", index=False)

print("✅ Sentiment prediction completed and saved!")
