#fa75c7e3bfe34bbcb33b3148d5a80d64
import requests
from pprint import pprint
class NewsFeed():
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "fa75c7e3bfe34bbcb33b3148d5a80d64"
    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.language = language
        self.from_date = from_date
        self.to_date = to_date
    def get(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"Language={self.language}&" \
              f"apiKey={self.api_key}"
        response = requests.get(url)
        content = response.json()
        articles = content['articles']

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + '\n' + article['url'] + "\n\n"

        return email_body

newsfeed = NewsFeed(interest="Nasa", from_date="2021-07-27", to_date="2021-08-17", language="en").get()
print(newsfeed)