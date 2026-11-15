import requests
import os
from dotenv import load_dotenv

load_dotenv()

def speak_news():

    api_key = os.getenv("NEWS_API_KEY")

    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "country": "us",
        "category": "general",
        "apiKey": api_key,
        
    }

    response = requests.get(url, params=params)

    data = response.json()
    print("API Status:", response.status_code)
    

    articles = data["articles"]

    headlines = []

    for article in articles:
        headlines.append(article["title"])

    return headlines