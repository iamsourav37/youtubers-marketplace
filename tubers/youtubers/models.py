from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class Youtuber(models.Model):

    CREW_CHOICES = (
        ('solo', 'Solo'),
        ('small', 'Small'),
        ('large', 'Large'),
    )

    CATEGORY_CHOICES = (
        ('teaching', 'Teaching'),
        ('mobile review', 'Mobile |Review'),
        ('technology', '|Technology'),
        ('cooking', 'Cooking'),
        ('vlogs', 'Vlogs'),
        ('moto vlogging', 'Moto Vlogging'),
        ('comedy', 'Comedy'),
        ('roasting', 'Roasting'),
        ('religious', 'Religious'),
        ('audio story', 'Audio Story'),
        ('other', 'Other'),
    )

    CAMERA_TYPE = (
        ('Cannon', 'Cannon'),
        ('Sony', 'Sony'),
        ('Go Pro', 'Go Pro'),
        ('DSLR', 'DSLR'),
        ('Other', 'Other'),

    )


    name = models.CharField(max_length=255)
    price = models.IntegerField()
    photo = models.ImageField(upload_to="media/ytubers/%Y/%m")
    video_url = models.CharField(max_length=1000, default=f"https://www.youtube.com/link")
    description = RichTextField()
    city = models.CharField(max_length=255)
    age = models.IntegerField()
    height = models.FloatField()
    crew = models.CharField(max_length=255, choices=CREW_CHOICES, default=CREW_CHOICES[0][0])
    camera_type = models.CharField(max_length=255, choices=CAMERA_TYPE, default=CAMERA_TYPE[0][0])
    subs_count = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0])
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self) -> str:
        return self.name

