# Generated by Django 3.2.8 on 2021-10-25 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiretuber',
            name='tuber_id',
            field=models.IntegerField(null=True),
        ),
    ]
