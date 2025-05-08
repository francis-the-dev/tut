from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class tutor_model(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tutor_m')
    number = models.IntegerField()
    expertise = models.CharField(max_length=64)
    unit = models.TextField()
    profile = models.ImageField(upload_to='profile_image')
    price_per_hour = models.IntegerField(default=0)
    transcript = models.ImageField(upload_to='transcript')

