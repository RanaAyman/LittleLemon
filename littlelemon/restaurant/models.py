from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return self.title
    
    def get_item(self):
        return f'{self.title} : {str(self.price)}'
