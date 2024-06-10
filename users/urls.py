from django.urls import path

from . import views

# from rest_framework.routers import DefaultRouter
#
#
# router = DefaultRouter()
# router.register('users', views.UserListAPIView.as_view())


urlpatterns = [
	path('list/', views.UserListAPIView.as_view(), name='users-list')
]
