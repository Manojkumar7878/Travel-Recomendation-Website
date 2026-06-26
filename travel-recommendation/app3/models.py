# AFTER
from django.db import models
from django.contrib.auth.models import User   # ✅ add this import

class Datas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # ✅ add this line
    starting = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    seat = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('starting', 'destination', 'date')

    def __str__(self):
        return f"{self.starting} to {self.destination} on {self.date}"

class Place(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='places/images/')
    description = models.TextField()

    def __str__(self):
        return self.title
    
class BusRoute(models.Model):
    starting = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.TimeField()
    arrival_time = models.TimeField()
    seat_capacity = models.IntegerField(default=40)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    bus_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.bus_name}: {self.starting} → {self.destination}"
    
    def available_seats(self, date):
        booked = Datas.objects.filter(
            starting__iexact=self.starting,
            destination__iexact=self.destination,
            date=date
        ).count()
        return self.seat_capacity - booked