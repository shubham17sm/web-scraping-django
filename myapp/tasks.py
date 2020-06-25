from __future__ import absolute_import, unicode_literals

import requests
from time import sleep
import csv
import os
from bs4 import BeautifulSoup

from celery import shared_task
from .models import News

from fake_useragent import UserAgent


@shared_task
def news_task():
    print('Collecting news article..')
    urls = ['https://timesofindia.indiatimes.com/rssfeeds/1221656.cms',
            'https://www.hindustantimes.com/rss/topnews/rssfeed.xml']

    user_agent = UserAgent()

    for url in urls:
        r = requests.get(url, headers={"user-agent": user_agent.chrome})
        htmlcontent = r.content
        # print(htmlcontent)

        soup = BeautifulSoup(htmlcontent, "xml")
        # print(soup.prettify)

        rows = soup.find_all('item')

        for row in rows:
            title = row.find('title').get_text()
            description = row.find('description').get_text()
            link = row.find('link').get_text()
            guid = row.find('guid').get_text()
            pubdate = row.find('pubDate').get_text()

            print({'title': title, 'description': description,
                   'link': link, 'guid': guid, 'pubdate': pubdate})

            News.objects.create(
                title=title,
                description=description,
                link=link,
                pubdate=pubdate,
                news_bool=False
            )

            sleep(5)


news_task()
