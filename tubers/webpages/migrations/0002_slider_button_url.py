# Generated by Django 3.2.8 on 2021-10-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='button_url',
            field=models.URLField(default='#'),
        ),
    ]
