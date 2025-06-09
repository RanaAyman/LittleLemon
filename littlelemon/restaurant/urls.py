from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables/booking', views.BookingViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    
    # path('menu/', views.menuview.as_view()),
    # path('booking/', views.bookingview.as_view()),
    
    path('api-token-auth/', obtain_auth_token),
    
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    
    path('menu/', views.MenuItemsView.as_view(), name="menu"),
    path('menu_item/<int:pk>', views.SingleMenuItemView.as_view(), name="menu_item"),
    
    path('', include(router.urls)),
    
    path('book/', views.book, name="book"), 
    path('bookings', views.bookings, name='bookings'),
    path('reservations/', views.reservations, name="reservations"),

]
