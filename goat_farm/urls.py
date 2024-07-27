from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from goat_farm.views import (custom_user_views, goat_views, health_views,
                             register_views)

urlpatterns = [
    path('user/', custom_user_views.CustomUserList.as_view()),
    path('user/<int:pk>/', custom_user_views.CustomUserDetail.as_view()),
    path('goat/', goat_views.GoatList.as_view()),
    path('goat/<int:pk>/', goat_views.GoatDetail.as_view()),
    path('goat/', goat_views.GoatList.as_view()),
    path('goat/<int:pk>/', goat_views.GoatDetail.as_view()),
    path('health/', health_views.HealthList.as_view()),
    path('health/<int:pk>/', health_views.HealthDetail.as_view()),
    path('logout/', register_views.CustomLogoutView.as_view(), name='logout'),
    path('api/token', register_views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair')
]

urlpatterns = format_suffix_patterns(urlpatterns)
