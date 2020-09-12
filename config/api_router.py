from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from main.views import CategoryViewSet, AuthorViewSet, PostViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'authors', AuthorViewSet, basename='authors')

app_name = "api"
urlpatterns = router.urls
