from django.urls import path
from .views import HomePageView, AboutPageView, ContactView, SellsView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contacts"),
    path('sells/', SellsView.as_view(), name='Sells'),
]
