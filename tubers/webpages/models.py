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