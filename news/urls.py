from django.urls import path

from .views import (
	CategoryView,
	CategoryNewsView,
	NewsView,
	NotificationView,
	UserNotifiedView,
	NotificationListView,
	MyPreferenceView
	)


urlpatterns = [
    path('get/<slug:title>/', NewsView.as_view(),
		name='get-news'),
    path('category/', CategoryView.as_view(),
    	name='news-category'),
    path('category/<slug:category>/', CategoryNewsView.as_view(),
    	name='news-category-news'),
    path('notification/', NotificationView,
    	name='news-notification'),
    path('update-notification/', UserNotifiedView,
    	name='update-news-notification'),
    path('notification-list/', NotificationListView.as_view(),
    	name='news-notification-list'),
    path('my-preference/', MyPreferenceView.as_view(),
    	name='news-my-preference'),
]
