from django.shortcuts import render, redirect

from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import News


def index(request):
    qs = News.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(qs, 5)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
        
    context = {
       'qs': qs,
       'news': news
    }
    return render(request, "news.html", context)