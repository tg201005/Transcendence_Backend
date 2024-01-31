from django.urls import path
from .views import UserOrTokenAPIView, LoginAPIView, OAuthCallbackAPIView, LogOutAPIView, home, check_login_status

urlpatterns = [
    path('home/', home, name='home'),
    path('api/v1/user-or-token/', UserOrTokenAPIView.as_view(), name='user-or-token'),
    path('api/v1/check-login', check_login_status, name='check-login'),
    path('login-url/', LoginAPIView.as_view(), name='login-url'),
    path('logout/', LogOutAPIView.as_view(), name='logout-url'),
    path('oauth/', OAuthCallbackAPIView.as_view(), name='oauth-callback'),
]
