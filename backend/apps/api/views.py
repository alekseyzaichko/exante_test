
from rest_framework import generics
from apps.news.models import Category, News
from .serializers import CategorySerializer, NewsListSerializer, NewsDetailsSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import pagination


class CategoryList(generics.ListAPIView):
    """
    Category Data API
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class Pagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100


class NewsList(generics.ListAPIView):
    """
    News List Data API
    """
    serializer_class = NewsListSerializer
    pagination_class = Pagination

    def get_queryset(self):
        category_slug = self.request.query_params.get('category', None)
        category = Category.objects.filter(slug=category_slug).first()
        return (category.news.all() if category else News.objects.all()).order_by('-datetime')


class NewsDetails(generics.RetrieveAPIView):
    """
    News Details Data API
    """
    serializer_class = NewsDetailsSerializer
    queryset = News.objects.all()

