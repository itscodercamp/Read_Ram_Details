from django.db import models


class Registration(models.Model):
    Name = models.CharField(max_length=150 ,blank=True,null=True)
    Email = models.EmailField(blank=True,null=True)
    Number = models.IntegerField(blank=True,null=True)
    Password = models.CharField(max_length=150,blank=True,null=True)

    def __str__(self):
        return self.Email
    