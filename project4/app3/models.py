from django.db import models

class Signup(models.Model):
    user = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=255)
    pasw = models.CharField(max_length=255)  # Use hashed password only, don't set unique here

    def __str__(self):
        return self.user
    

class Datas(models.Model):
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
