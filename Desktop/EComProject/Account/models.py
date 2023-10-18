from django.db import models
from core_uuid.models import BaseModel
from django.contrib.auth.models import User
# Create your models here.

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,related_name='profile')
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=120,null=True,blank=True)
    profile_image = models.ImageField(upload_to='profile')