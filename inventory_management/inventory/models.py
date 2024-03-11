from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    short_name= models.CharField(max_length=10)
    logopath = models.CharField(max_length=200)

    def __str__(self):
        return self.short_name
    

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=100)
    iconpath = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    name = models.CharField(max_length=100)
    logopath = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class System(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    logopath = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class InventoryItem(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
    model = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=100)
    operatyng_system = models.ForeignKey('System', on_delete=models.DO_NOTHING)
    location = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        

