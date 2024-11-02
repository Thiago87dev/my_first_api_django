from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HelloDRFView, ItemViewSet, CategoryViewSet, AddView

router = DefaultRouter()

router.register(r'items', ItemViewSet, basename='item')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'adds', AddView, basename='add')

urlpatterns = [
    path('hello/', HelloDRFView.as_view(), name='hello_drf'),
    path('api/', include(router.urls,)),  # Todas as rotas do router serão prefixadas com 'api/'
]
