from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Bids(models.Model):
    current_bid = models.FloatField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Listing(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=255)
    image_url = models.URLField(max_length=2000, blank=True, null=True) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    starting_bid = models.FloatField()
    all_bids= models.ManyToManyField(Bids)
    sold = models.BooleanField(default=False)
    watchlist = models.ManyToManyField(User, related_name= "watchlist")
    listed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_listings", null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True, related_name='comments')
    comment = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.comment


