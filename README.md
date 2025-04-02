# NYT Sentiment Analysis Dashboard

## 📌 Project Overview
This project analyzes the sentiment of the most popular New York Times articles using a **Logistic Regression model**. The data is fetched via the NYT Most Popular API, and sentiment predictions are visualized using a **dashboard**.

## 📂 Project Structure
```
├── Artifacts
│   ├── tfidf_vectorizer.pkl  # TF-IDF Vectorizer
│   ├── logistic_regression_model.pkl  # Trained Logistic Regression Model
│
├── datasets
│   ├── nyt_articles.csv  # Monthly appended data
│   ├── nyt_most_with_sentiment.csv  # it has sentiment for a given article
│
├── dashboard
│   ├── dashboard.py  # Streamlit dashboard for visualization
│
├── envs
│   ├── requirements.txt  # Dependencies
│   ├── nyt_sentiment.yml  # Conda environment file
│
├── python_files
│   ├── fetch_data.py  # Fetches data from NYT API
│   ├── new_data_monthly_append.py  # Appends latest data
│   ├── predict.py  # Predicts sentiment for articles
│   ├── train.py  # Trains Logistic Regression model
```

## 🛠 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Create and Activate Conda Environment
#### Using `requirements.txt`
```bash
conda create --name nyt_sentiment python=3.9
conda activate nyt_sentiment
pip install -r envs/requirements.txt
```
#### Using `nyt_sentiment.yml`
```bash
conda env create -f envs/nyt_sentiment.yml
conda activate nyt_sentiment
```

### 3️⃣ Fetch Data from NYT API
Replace `YOUR_API_KEY` in `fetch_data.py` and run:
```bash
python python_files/fetch_data.py
```
This will download the latest NYT Most Popular articles and store them in `datasets/nyt_most_popular.csv`.

### 4️⃣ Train the Sentiment Model
```bash
python python_files/train.py
```
This will train a **Logistic Regression model** and save it in the `Artifacts/` folder.

### 5️⃣ Predict Sentiments
```bash
python python_files/predict.py
```
This script loads new articles, vectorizes them, and predicts sentiments using the trained model.

### 6️⃣ Update Data Monthly
```bash
python python_files/new_data_monthly_append.py
```
This script appends the latest one-month data to `nyt_most_popular.csv`.

### 7️⃣ Run the Dashboard
```bash
streamlit run dashboard/dashboard.py
```
This will launch a **Streamlit dashboard** in the browser to visualize sentiment trends.

## 📌 Key Features
✅ Fetches real-world news data from **NYT API**
✅ Applies **Logistic Regression** for sentiment classification
✅ **Automated monthly updates** for long-term analysis
✅ Interactive **Streamlit Dashboard** for visualization

## 🤝 Contributing
Feel free to fork the repo, create issues, and submit pull requests!

## 📜 License
This project is licensed under the MIT License.

---
_🚀 Happy Coding!_