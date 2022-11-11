from django.urls import path
from .views import BlogListView, BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/',  BlogDeleteView.as_view(), name='post_detail'),
]