from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from twitter.viewsets import user_viewset
from twitter.viewsets import post_viewset


router = routers.DefaultRouter()
router.register('users', user_viewset.UserViewSet, basename='user')
router.register('post', post_viewset.PostViewSet, basename='post')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', user_viewset.UserViewSet.as_view({'post': 'login'}), name='login'),
    path('', include(router.urls)),
]
