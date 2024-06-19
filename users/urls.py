from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

# from rest_framework.routers import DefaultRouter
#
#
# router = DefaultRouter()
# router.register('users', views.UserListAPIView.as_view())


urlpatterns = [
	path('list/', views.UserListAPIView.as_view(), name='users-list'),
	path('create/', views.UserRegisterView.as_view(), name='user-register'),
	path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	path('logout/', views.UserLogoutView.as_view(), name='user-logout')
]
