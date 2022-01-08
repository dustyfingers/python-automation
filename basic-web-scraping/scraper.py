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
    
    retval  = '>> HackerNews Top Stories <<'
    
    retval += '\n\n\n'

    response = requests.get(url)

    content = response.content
    soup = BeautifulSoup(content, 'html.parser')

    parsed_soup = soup.find_all('td', attrs={'class': 'title', 'valign': ''})

    for i, tag in enumerate(parsed_soup):
        retval += ((str(i + 1) + ' :: ' + tag.text + '\n') if tag.text != 'More' else '')
    
    return retval

content += extract_news('https://www.hackernews.com')

print(content)