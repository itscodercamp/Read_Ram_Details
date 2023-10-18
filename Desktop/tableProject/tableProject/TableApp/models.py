# from django.db import models

# # Create your models here.
# class Employee(models.Model):
#     name = models.CharField(max_length=105,blank=True,null=True)
#     email = models.EmailField(blank=True,null=True)
#     number = models.IntegerField(blank=True,null=True)
#     DOB = models.DateField(blank=True,null=True)
#     city = models.CharField(max_length=105,blank=True,null=True)
#     pin = models.IntegerField(blank=True,null=True)

#     def __str__(self):
#         return self.name

from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    number = models.CharField(max_length=15,null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    pin = models.CharField(max_length=10,null=True,blank=True)

    def __str__(self):
        return self.name
