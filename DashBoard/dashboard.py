import streamlit as st
import pandas as pd
import pickle
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

# # Download stopwords
# nltk.download("stopwords")

# Load model & vectorizer
with open("Artifacts/logistic_regression_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("Artifacts/tfidf_vectorizer.pkl", "rb") as vec_file:
    vectorizer = pickle.load(vec_file)

# Preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    text = " ".join([word for word in text.split() if word not in stopwords.words("english")])
    return text

# Streamlit UI
st.title("NYT Sentiment Analysis Dashboard 📰")

st.write("Enter an article's abstract below to analyze its sentiment.")

user_input = st.text_area("Enter Text:", "")

if st.button("Analyze Sentiment"):
    if user_input:
        cleaned_text = preprocess_text(user_input)
        transformed_text = vectorizer.transform([cleaned_text])
        prediction = model.predict(transformed_text)[0]
        
        st.subheader(f"Predicted Sentiment: **{prediction.upper()}**")
    else:
        st.warning("Please enter some text!")

# Show existing dataset
st.write("### Sentiment Analysis on Recent NYT Articles")
df = pd.read_csv("Datasets/nyt_articles_with_sentiment.csv")
st.dataframe(df[["published_date", "abstract", "predicted_sentiment"]])
