from django.db import models

# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)


    def __str__(self):
        return self.name


class Watchlist(models.Model):
    title = models.CharField(max_length=30)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE, related_name='watchlist')
    active = models.BooleanField(default=True) # if the content is release or launched
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

