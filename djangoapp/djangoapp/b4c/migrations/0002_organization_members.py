# Generated by Django 4.2.1 on 2023-05-08 10:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('b4c', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
