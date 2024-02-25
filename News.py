import requests
import json

query = input("What type of News are you interested in: ")
print("\n")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-08-17&sortBy=publishedAt&apiKey=d1869029cddb47da8ab9039dca0a6d87"

r = requests.get(url)

if r.status_code == 200:
    news = json.loads(r.text)
    if news['totalResults'] > 0:
        for article in news["articles"]:
            print(article["title"])
            print(article["description"])
            print("\n")
            print("================================================================================================")
            print("\n")
    else:
        print("No articles found for the given query.")

else:
    print(f"Failed to fetch news. Status code: {r.status_code}")
