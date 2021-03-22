from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *



router = DefaultRouter()
router.register('image', ImageViewSet)

urlpatterns = [
    path('list/', TopperView.as_view(), name='topper_list'),
    path('create/', TopperCreate.as_view(), name='topper_create'),
    path('detail/<int:pk>/', TopperDetail.as_view(), name='topper_detail'),
    path('edit/<int:pk>', TopperEdit.as_view(), name='topper'),
    path('topper/<int:pk>', TopperDetailView.as_view(), name='topper'),
    path('comments/create/', CommentaryCreateView.as_view(), name='commentary_create'),

    path('comments/list/', AdView.as_view(), name='ad_list'),
    path('comments/create/', AdCreate.as_view(), name='ad_create'),
    path('ad/<int:pk>/', AdDetail.as_view(), name='ad_detail'),
    path('comments/edit/<int:pk>', AdEdit.as_view(), name='ad_edit'),

    path('', include(router.urls)),

]