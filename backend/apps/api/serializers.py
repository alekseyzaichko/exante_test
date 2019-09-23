from rest_framework import serializers

from apps.news.models import Category, News

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class BaseNewsSerializer(serializers.ModelSerializer):
    datetime = serializers.SerializerMethodField()

    def get_datetime(self, obj):
        return obj.datetime.strftime('%d.%m.%Y')


class NewsListSerializer(BaseNewsSerializer):
    class Meta:
        model = News
        fields = ('id', 'category_id', 'title', 'datetime')


class NewsDetailsSerializer(BaseNewsSerializer):
    class Meta:
        model = News
        fields = ('id', 'category_id', 'title', 'content', 'image', 'datetime')
