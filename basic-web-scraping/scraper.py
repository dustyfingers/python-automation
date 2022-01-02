import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

now = datetime.datetime.now()

content = ''


# extracts current news from Hacker News
def extract_news(url):
    print("Extracting HackerNews stories...")
    
    retval  = '<b>HackerNews Top Stories</b>\n<br>-'*50 + '<br>'

    response = requests.get(url)

    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    parsed_soup = soup.find_all('td', attrs={'class': 'title', 'valign': ''})

    for i, tag in enumerate(parsed_soup):
        retval += ((str(i + 1) + ' :: ' + tag.text + '\n<br>') if tag.text != 'More' else '')
    
    return retval


print(extract_news('https://www.hackernews.com'))