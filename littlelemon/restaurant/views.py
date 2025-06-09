from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Booking, MenuItem
from .serializers import BookingSerializer, UserSerializer, MenuItemSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets, generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import BookingForm
from rest_framework.decorators import action
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

# class bookingview(APIView):
    
#     def get(self, request):
#         items = Booking.objects.all()
#         serializer = BookingSerializer(items, many=True)
#         return Response(serializer.data)
    
# class menuview(APIView):
    
#     def post(self, request):
#         serializer = MenuItemSerializer(data = request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status":"success", "data":serializer.data})

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Restricts access to authenticated users

# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    def get(self, request):
        menu_data = MenuItem.objects.all()
        return render(request, 'menu.html', {"menu": {"menu": menu_data}})

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    def get(self, request, pk=None):
        menu_item = MenuItem.objects.get(pk=pk) if pk else None
        return render(request, 'menu_item.html', {"menu_item": menu_item})

@permission_classes([IsAuthenticated])  
@api_view(['GET'])
def reservations(request):
    # date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

@permission_classes([IsAuthenticated]) 
@api_view(['GET','POST'])
def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

@permission_classes([IsAuthenticated]) 
@api_view(['GET','POST'])
@csrf_exempt
def bookings(request):
    if request.method == "POST":
        data = json.load(request)
        exist = Booking.objects.filter(booking_date=data['booking_date']).filter(reservation_slot = data['reservation_slot']).exists()
        if not exist:
            booking = Booking(name=data['name'],booking_date=data['booking_date'],reservation_slot=data['reservation_slot'], number_of_guests=data['number_of_guests'])
            booking.save()
        else:
            HttpResponse("{'error':1}", content_type = 'application/json')
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all().filter(booking_date=date)
    booking_json = serializers.serialize('json', bookings)
    return HttpResponse(booking_json, content_type = 'application/json') 

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated] 
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
