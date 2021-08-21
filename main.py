import yagmail
import pandas as pd
from news import NewsFeed

df = pd.read_excel("people.xlsx")
for index,row in df.iterrows():
    news_feed = NewsFeed(interest=row['interest'], from_date="2021-07-27", to_date="2021-08-17", language="en")

    email = yagmail.SMTP(user="laptop2315051@gmail.com", password="lap_top_2315051")
    email.send(to=row['email'],
               subject=f"Hi! Your {row['interest']} news today.",
               contents=f" hi {row['name']} \n see whats on about {row['interest']} today {news_feed.get()}")