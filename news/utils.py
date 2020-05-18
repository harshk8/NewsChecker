import json
import requests
from django.http import JsonResponse
from django.views.generic import ListView
from django.shortcuts import render, HttpResponse
from django.db.models import Count, F, Max, Q, signals
from django.contrib.auth.decorators import login_required

from .models import NewsCategory, News, NewsSource, Notification


def fetch_data(request, query=None, fromdate=None,
    todate=None, category=None):
    """
    Fetch News from different platforms
    """

    filter_query = 'top-headlines?language=en'
    if query:
        filter_query += '&q='+query
    if fromdate:
        filter_query += '&formdate='+str(fromdate.strftime("%Y-%m-%d"))
    if todate:
        filter_query += '&todate='+str(todate.strftime("%Y-%m-%d"))
    if category:
        filter_query += '&category='+category.lower()

    #TODO: add API field in NEWS SOUCRCE MODEL
    sources = NewsSource.objects.all()

    for source in sources:

        if source.api_key:
            filter_query+='&apiKey='+source.api_key

        data = requests.get(source.url+filter_query)

        if data.status_code == 200:
            data = json.loads(data.content)
            store_data(request,data['articles'], category=category)


def store_data(request, data, category=None):
    """
    Store data of news gathered from different platform
    """
    all_news = News.objects.values_list('title', flat=True)
    all_news = set(news for news in all_news)
    category = NewsCategory.objects.get(title=category)
    
    for dd in data:
        if not dd['title'] in all_news:
            news = News()
            news.title = dd['title']
            news.description = dd['description']
            news.relavent_url = dd['url']
            news.relavent_image = dd.get('urlToImage',None)
            news.date = dd.get('publishedAt', None)
            news.category = category
            if dd.get('author'):
                news.author = dd.get('author', 'NA')
            news.save()

            related_users = category.user.all()

            for user in related_users:

                if not Notification.objects.filter(
                    title__icontains=dd['title'][:100],
                    user=user.user).exists():

                    Notification.objects.create(
                        url=news.relavent_url, 
                        title=news.title[:100],
                        user=user.user)
