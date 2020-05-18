from datetime import datetime
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib import messages
from django.views.generic.list import ListView, View
from django.views.generic.edit import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views.generic import ListView
from news.models import News, NewsCategory
from django.contrib.auth.models import User
from news.utils import fetch_data


class DashboardView(ListView):
    """
    Get and search latest news on dashboard
    """
    model = News
    template_name = 'users/dashboard.html'

    def get(self, request):
        news = self.model.objects.all().order_by('-created_at')
        category_list = NewsCategory.objects.all()
        return render(request, self.template_name , context={
            'object_list':news, 'category_list':category_list})

    def post(self, request, *args, **kwargs):
        query = request.POST.get('search', None)
        fromdate = request.POST.get('fromDate', None)
        todate = request.POST.get('toDate', None)
        category = request.POST.get('category', None)
 
        if fromdate:
            fromdate = datetime.strptime(fromdate, "%m/%d/%Y")

        if todate:
            todate = datetime.strptime(todate, "%m/%d/%Y")

        #We can put this method in BACKEND JOB using CELERY
        news = fetch_data(
            request, query=query, fromdate=fromdate,
            todate=todate, category=category)
        news = News.objects.filter(
            date__gte=fromdate,
            date__lte=todate,
            category__title__icontains=category)

        category_list = NewsCategory.objects.all()

        return render(request, 'users/dashboard.html', context={
            'object_list':news, 'category_list':category_list})


class AddPreferenceView(CreateView):
    """
    add new preference in list
    """
    model = NewsCategory

    def post(self, request, *args, **kwargs):
        cat = self.model.objects.get(
            title_slug=kwargs['category'])

        profile = request.user.profile
        profile.preferences.add(cat)
        profile.save()
        return redirect('news-category')



class RemovePreferenceView(CreateView):
    """
    remove preference from list
    """
    model = NewsCategory

    def post(self, request, *args, **kwargs):
        cat = self.model.objects.get(
            title_slug=kwargs['category'])

        profile = request.user.profile
        profile.preferences.remove(cat)
        profile.save()
        return redirect('news-category')