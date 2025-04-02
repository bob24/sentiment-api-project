import requests
import pandas as pd
from datetime import datetime

API_KEY = "A8DoYbK5bVZ8KKKFnGRftmCKegAg4Jwk"
BASE_URL = "https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key=" + API_KEY

# Get the last month's year and month
today = datetime.today()
last_month = today.month - 1 if today.month > 1 else 12
last_year = today.year if today.month > 1 else today.year - 1

print(f'last_month: {last_month}, last_year: {last_year}')

api_url = BASE_URL.format(year=last_year, month=last_month)
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    articles = data["response"]["docs"]
    
    new_articles = []
    for article in articles:
        new_articles.append({
            "id": article["_id"],
            "published_date": article["pub_date"],
            "headline": article["headline"]["main"],
            "abstract": article["abstract"],
            "url": article["web_url"],
            "section": article.get("section_name", "Unknown")
        })
    
    # Load existing CSV
    df_existing = pd.read_csv("Datasets/nyt_articles.csv")
    
    # Convert to DataFrame
    df_new = pd.DataFrame(new_articles)
    
    # Append new data and drop duplicates
    df_combined = pd.concat([df_existing, df_new]).drop_duplicates(subset=["id"])
    
    # Save updated file
    df_combined.to_csv("Datasets/nyt_articles.csv", index=False)
    print(f"✅ Added {len(new_articles)} new articles for {last_year}-{last_month}")
else:
    print(f"❌ Error fetching data for {last_year}-{last_month}")
