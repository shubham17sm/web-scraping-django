# web-scraping-django
A news aggregator app build using [Django](https://www.djangoproject.com/) web framework and [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) which is use to scrape the news articles from the web and uses [celery](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html) as a task queue to add srcaped article in database. This app is also provided with API using [Django rest-framework](https://www.django-rest-framework.org/)



# Getting Started

First Create and start your virtual environment:
Clone or download this repository
```
  virtualenv -p python3 .
  pip install -r requirement.txt
  python3 manage.py runserver

```

Command for starting worker process in celery:
```
celery -A myproject worker --loglevel=info

```

# Post Installation
Go to the web browser and visit http://127.0.0.1:8000/

Admin username: admin

Admin password: admin

