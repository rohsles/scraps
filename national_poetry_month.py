from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests
import random
import smtplib


#base link variables
content_url = "http://april-is.tumblr.com/post/369115634/master-list-of-april-is-poems"
content_links = []

#email variables
me = email
msg = MIMEMultipart('alternative')
msg['Subject'] = "Poem of the Day"

def get_text(url):

    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    return soup

def get_content_links():
    
    soup = get_text(content_url)
    for link in soup.find_all('a'):
        href = link.get('href')
        if 'post' in href and 'master' not in href: 
            content_links.append(href)
    return content_links

def get_content():

    random_url = random.choice(content_links)
    soup = get_text(random_url)
    content = soup.find_all('div', attrs={'class': 'content'})
    return random_url, content[0]

def generate_mail():

    content_links = get_content_links()
    random_url, content = get_content()
    msg.attach(MIMEText(random_url, 'plain'))
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(username, password)
    mail.sendmail(me, me, msg.as_string())
    mail.quit()

if __name__ == '__main__':

    generate_mail()
