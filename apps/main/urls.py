from django.urls import path
from .views import HomeView, ContactView, ForumView

app_name = 'main'

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("contact/", ContactView.as_view(), name='contact'),
    path("forum/", ForumView.as_view(), name='forum'),
]
