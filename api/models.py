from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Adminstration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13)
    photo = models.ImageField(upload_to="profile_pic", default="default.jpg")
    company_name = models.CharField(max_length=250)

    def __str__(self) :
        return f'{self.user.first_name} works in {self.company_name}'
    
class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250)
    station = models.CharField(max_length=250)
    phone = models.CharField(max_length=13)
    photo = models.ImageField(upload_to="profile_pic", default="default.jpg")
    def __str__(self) :
        return f'{self.user.first_name} works at {self.station}'
    
class Company(models.Model):
    company_name = models.CharField(max_length=250)
    web_link = models.CharField(max_length=250)
    logo = models.ImageField(upload_to="logo", default="logo.jpg")
    description = models.TextField()

    def __str__(self) -> str:
        return self.company_name
    
class Bus(models.Model):
    license_plate = models.CharField(max_length=250)
    driver = models.CharField(max_length=250)
    num_of_seats = models.IntegerField()
    level = models.IntegerField()
    description = models.TextField()
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name="bus_of_company")

    def __str__(self):
        return self.license_plate
    
class AvailableBus(models.Model):
    date = models.DateTimeField()
    source = models.CharField(max_length=250)
    destination= models.CharField(max_length=250)
    bus = models.ForeignKey(Bus,on_delete=models.PROTECT,related_name='list_of_buses')

    def __str__(self):
        return f'{self.date.date()}--{self.bus.license_plate}'
    
class Ticket(models.Model):
    source = models.CharField(max_length=250)
    destination= models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=13)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    seat_num = models.IntegerField()

    def __str__(self):
        return f'{self.name} ticket'
   


