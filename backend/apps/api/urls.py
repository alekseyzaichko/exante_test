from django.urls import path
from .views import CategoryList, NewsList, NewsDetails

urlpatterns = [
    path('categories/', CategoryList.as_view(), name="categories"),
    path('news/', NewsList.as_view(), name="news_list"),
    path('news/<int:pk>/', NewsDetails.as_view(), name="news_details"),
]