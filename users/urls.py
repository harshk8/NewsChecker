from django.urls import path

from .views import (
	DashboardView,
	AddPreferenceView,
	RemovePreferenceView
	)


urlpatterns = [
    path('', DashboardView.as_view(), name='user-dashboard'),
    path('<slug:category>/add/', AddPreferenceView.as_view(),
    	name='user-add-preference'),
    path('<slug:category>/remove/', RemovePreferenceView.as_view(),
    	name='user-remove-preference'),
]
