from django.urls import path
from .views import HomePageView, get_queryset
from bot import views
urlpatterns = [
    path('bot/', get_queryset, name='search_results'),
    path('', HomePageView.as_view(), name='home'),
]