from django.contrib import admin
from .models import NewsCategory, News, NewsSource, Notification


admin.site.register(News)
admin.site.register(NewsCategory)
admin.site.register(NewsSource)
admin.site.register(Notification)