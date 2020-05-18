import json
import requests
from django.http import JsonResponse
from django.views.generic import ListView
from django.shortcuts import render, HttpResponse
from django.db.models import Count, F, Max, Q, signals
from django.contrib.auth.decorators import login_required

from .utils import fetch_data
from .models import NewsCategory, News, NewsSource, Notification


class CategoryView(ListView):
    """
    Get list of category
    """
    model = NewsCategory
    template_name = 'news/category.html'
    paginate_by = 10


class MyPreferenceView(ListView):
    """
    Get list of my category / preferences
    """
    model = NewsCategory
    template_name = 'news/category.html'
    paginate_by = 10

    def get_queryset(self):
        return self.request.user.profile.preferences.all()


class NotificationListView(ListView):
    """
    Get list of notifications
    """
    model = Notification
    template_name = 'news/notification.html'
    paginate_by = 10

    def get_queryset(self):
        return self.request.user.notification_set.all().order_by('-created_at')


class NewsView(ListView):
    """
    Get Individual news in detail
    """
    model = News
    template_name = 'news/news.html'

    def get(self, request, *args, **kwargs):
        news = None
        news = self.model.objects.filter(title_slug=kwargs['title'])
        
        if news:
            return render(request, self.template_name, context={
                'object': news[0], 'message':''})        
        return render(request, self.template_name, context={
            'object': news, 'message':'No News Found'})


class CategoryNewsView(ListView):
    """
    Get News on basis of category
    """
    model = News
    template_name = 'news/category_news_list.html'

    def get(self, request, *args, **kwargs):

        news = self.model.objects.filter(
            category__title_slug=kwargs['category'])

        is_preference = request.user.profile.preferences.filter(
            title_slug=kwargs['category']).exists()

        return render(request, self.template_name,
         context={
             'object_list': news,
             'is_preference':is_preference,
             'category':kwargs['category']
             }
        )


def NotificationView(request):
    """
    Get notification count
    """
    username = request.GET.get('username', None)
    notify = []
    if username:
        notify = Notification.objects.filter(
            is_seen=False, user__username=username).count()
    return JsonResponse({'notification':notify})


def UserNotifiedView(request):
    """
    Update seen status of notificaiton
    """
    username = request.GET.get('username', None)
    if username:
        notification = Notification.objects.filter(
            user__username=username).update(is_seen=True)
    return JsonResponse({'notified':True})
