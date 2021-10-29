from django.db import models

# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    company_name = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self) -> str:
        return f"{self.full_name}"


class SocialLink(models.Model):
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    fb_link = models.CharField(max_length=2000)
    insta_link = models.CharField(max_length=2000)
    twitter_link = models.CharField(max_length=2000)
    youtube_link = models.CharField(max_length=2000)

    def __str__(self) -> str:
        return f"{self.email}"



