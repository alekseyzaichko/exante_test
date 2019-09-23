from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="news")
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images', max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "news"

    def __str__(self):
        return self.title
