from django.urls import path
from .models import NewsArticle
from .views import NewsListView, NewsDetailView

urlpatterns = [
    path("", NewsListView.as_view(), name="list"),
    path("<int:pk>/detailview", NewsDetailView.as_view(), name="detail")
]