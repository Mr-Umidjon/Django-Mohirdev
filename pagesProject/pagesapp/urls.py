from django.urls import path
from .views import HomePageView, AboutPageView, ContactView, SellsView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="About"),
    path('contact/', ContactView.as_view(), name="About"),
    path('sells/', SellsView.as_view(), name='Sells'),
]
