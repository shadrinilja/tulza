from django.urls import path
from .views import SearchResultsView, HomePageView
urlpatterns = [
    path('bot/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
]