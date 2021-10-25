from django.db import models

# Create your models here.


class Hiretuber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    tuber_id = models.IntegerField(null=True)
    tuber_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(null=True)
    user_id = models.IntegerField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.email}"

    
