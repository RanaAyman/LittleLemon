from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    # path('menu/', views.menuview.as_view()),
    # path('booking/', views.bookingview.as_view()),
    path('api-token-auth/', obtain_auth_token)
]
