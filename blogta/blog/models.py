from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_superuser': True})
    categories = models.ManyToManyField(Category, related_name='articles')
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.commenter.email} on {self.article.title}"