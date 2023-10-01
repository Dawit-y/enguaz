from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Adminstration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    photo = models.ImageField(upload_to="profile_pic", default="default.jpg")
    company_name = models.CharField(max_length=250)

    def __str__(self) :
        return f'{self.user.first_name} works in {self.company_name}'
    
class Company(models.Model):
    company_name = models.CharField(max_length=250)
    web_link = models.CharField(max_length=250)
    logo = models.ImageField(upload_to="logo", default="logo.jpg")
    description = models.TextField()

    def __str__(self) -> str:
        return self.company_name
    
class Station(models.Model):
    place = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.place

class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=13)
    photo = models.ImageField(upload_to="profile_pic", default="default.jpg")
    station = models.ForeignKey(Station, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company_worker")
    def __str__(self) :
        return f'{self.user.first_name} works at {self.station}'


class Bus(models.Model):
    license_plate = models.CharField(max_length=250)
    driver = models.CharField(max_length=250)
    num_of_seats = models.IntegerField()
    level = models.IntegerField()
    description = models.TextField()
    station = models.ForeignKey(Station, on_delete=models.PROTECT)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name="bus_of_company")
    is_availaible = models.BooleanField(default=True)
    is_listed = models.BooleanField(default=False)

    def __str__(self):
        return self.license_plate
    
class AvailableBus(models.Model):
    date = models.DateTimeField()
    source = models.CharField(max_length=250)
    destination= models.CharField(max_length=250)
    price = models.FloatField()
    bus = models.ForeignKey(Bus,on_delete=models.CASCADE,related_name='list_of_buses')
    added_by = models.ForeignKey(Worker, on_delete=models.PROTECT, related_name="added_bus")
    def __str__(self):
        return f'{self.date.date()}--{self.bus.license_plate}'


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=13)

    def __str__(self) -> str:
        return self.first_name

class Seat(models.Model):
    seat_number = models.IntegerField()
    is_occupied = models.BooleanField(default=False)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.seat_number}"

class Ticket(models.Model):
    source = models.CharField(max_length=250)
    destination= models.CharField(max_length=250)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="ticket")
    price = models.DecimalField(decimal_places=2, max_digits=6)
    seat_num = models.IntegerField()

    def __str__(self):
        return f'{self.name} ticket'

