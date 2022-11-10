from django.urls import path
from .views import homePageView, data_of_mine

urlpatterns = [
    path('', homePageView, name="Home"),
    path('aboutMe/', data_of_mine, name='aboutMe'),
]