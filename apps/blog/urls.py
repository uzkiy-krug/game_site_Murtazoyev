from django.urls import path
from .views import BlogListView, BlogDetailView


app_name = 'blog'


urlpatterns = [
    path('list/', BlogListView.as_view(), name='list', ),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail'),
]