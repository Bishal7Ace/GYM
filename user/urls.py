from django.urls import path
from user.views import *

urlpatterns = [
    path('users/', UserAPIView.as_view(), name='user-list'),
    path('auth/register/', RegistrationAPIView.as_view(), name='register'),
    path('auth/login/', LoginAPIView.as_view(), name='login'),
    path('auth/refresh/', RefreshAPIView.as_view(), name='token_refresh'),
    path('auth/blacklist/', BlacklistTokenAPIView.as_view(), name='token_blacklist'),
]