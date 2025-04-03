import requests
import pandas as pd
from datetime import datetime, timedelta

API_KEY = "A8DoYbK5bVZ8KKKFnGRftmCKegAg4Jwk" #use your key
BASE_URL = "https://api.nytimes.com/svc/archive/v1/{year}/{month}.json?api-key=" + API_KEY

# Get today's date and calculate the last 12 months
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

print(f'start_data: {start_date}, end_data: {end_date}')
# List to store all data
all_articles = []

# Loop through each month
for i in range(12):
    year = start_date.year
    month = start_date.month
    api_url = BASE_URL.format(year=year, month=month)
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        articles = data["response"]["docs"]
        
        for article in articles:
            all_articles.append({
                "id": article["_id"],
                "published_date": article["pub_date"],
                "headline": article["headline"]["main"],
                "abstract": article["abstract"],
                "url": article["web_url"],
                "section": article.get("section_name", "Unknown")
            })
        print(f"✅ Fetched {len(articles)} articles for {year}-{month}")
    else:
        print(f"❌ Failed to fetch data for {year}-{month}")
    
    # Move to the previous month
    start_date = start_date + timedelta(days=31)  # Jump to the next month

# Convert to DataFrame and save
df = pd.DataFrame(all_articles)
df.to_csv("Datasets/nyt_articles.csv", index=False)
print("✅ All data saved to nyt_articles.csv")
