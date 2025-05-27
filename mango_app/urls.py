"""
URL configuration for the Mango Surveillance application.

This module defines the URL patterns for routing requests to view functions/classes.
"""
from django.urls import path, re_path
from . import views

app_name = 'mango_app'

urlpatterns = [
    # Home page route
    path('', views.HomeView.as_view(), name='home'),
    
    # Main section routes
    path('pests-diseases/', views.MangoItemListView.as_view(), name='mango_items'),
    path('surveillance-guide/', views.SurveillanceView.as_view(), name='surveillance_guide'),  # Renamed!
    path('about/', views.AboutView.as_view(), name='about'),
    
    # Detail page route - using regex to capture numeric item_id
    re_path(r'^pests-diseases/(?P<item_id>\d+)/$', views.MangoItemDetailView.as_view(), name='mango_item_detail'),
]