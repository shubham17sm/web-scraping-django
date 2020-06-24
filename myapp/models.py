from django.db import models

# Create your models here.

class News(models.Model):
    title = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=250, null=True, blank=True)
    pubdate = models.CharField(max_length=100, null=True, blank=True)
    news_bool = models.BooleanField(default=False)


    def __str__(self):
        return self.title
