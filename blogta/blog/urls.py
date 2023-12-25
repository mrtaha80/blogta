from django.urls import path
from .views import add_article, ArticleDetailView, CommentCreateView, CommentUpdateView

urlpatterns = [
    path('add-article/', add_article, name='add_article'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<int:pk>/comment/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
]