from django.urls import path
from .views import PostListView, AuthorPostListView

urlpatterns = [
    path("category-posts/<int:pk>/", PostListView.as_view()),
    path("author-posts/<int:pk>/", AuthorPostListView.as_view()),
]
