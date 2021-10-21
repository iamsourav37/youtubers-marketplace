from django.db import models

# Create your models here.


class Slider(models.Model):
    headline = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100)
    button_text = models.CharField(max_length=100)
    button_url = models.URLField(default='#')
    photo = models.ImageField(upload_to="media/slider_images/%Y/")
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.headline



class Team(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=200)
    fb_link = models.URLField(default='#')
    insta_link = models.URLField(default='#')
    photo = models.ImageField(upload_to="media/team_images/%Y/%m/%d/")
    youtube_link = models.URLField(default="#")
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.first_name + self.last_name

