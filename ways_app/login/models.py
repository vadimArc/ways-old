import pickle
import base64

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True, default='default@test.com')
    username = models.CharField(max_length=30, unique=True)

class Cities(models.Model):
    city = models.CharField(max_length=30, default="dao1", unique="true")
    country = models.CharField(max_length=30, default="dao2")
    city_user = models.ManyToManyField(
        Profile
    )

class Places(models.Model):
    name = models.CharField(max_length=30, default="dao3")


class Lists(models.Model):
    name  = models.CharField(max_length=100, default="dao4")
    owner = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="owner_lists"
    )
    followers = models.ManyToManyField(
        Profile,
        related_name="followers_lists"
    )
    places = models.ManyToManyField(
        Places
    )
    city = models.ForeignKey(
        Cities,
        on_delete=models.CASCADE,
        default=0
    )

    #change to 1-m








#1. User adds city
#2. User selects city
#3. User adds items to the list

#1. Call FSQ API look for the city
#2. Check if the city is in DB
#3. Add city or add relationship Profile --- City
#
# Profile --> City --> list --> Places
#                     owner
#                     follower
