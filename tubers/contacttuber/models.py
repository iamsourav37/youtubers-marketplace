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