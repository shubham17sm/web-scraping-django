from django.shortcuts import render, redirect

import requests
import time
import csv
import os
from bs4 import BeautifulSoup

# Create your views here.
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

from .models import News

url = "https://timesofindia.indiatimes.com/rssfeeds/1221656.cms"

r = requests.get(url)
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



News.objects.create(
title = title,
description = description,
link = link,
pubdate = pubdate,
news_bool = False
)

# titles = soup.find_all('title')
# desps = soup.find_all('description')

# title_collect = []
# desp_collect = []

# for title in titles:
#     title_collect.append(title.text)

# for desp in desps:
#     desp_collect.append(desp.text)

def index(request):
    qs = News.objects.all()
    context = {
    #    'title_collect': title_collect,
    #    'desp_collect': desp_collect,
       'rows': rows,
       'qs': qs
    }
    return render(request, "news.html", context)