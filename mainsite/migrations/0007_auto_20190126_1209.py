# Generated by Django 2.1.1 on 2019-01-26 12:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_auto_20190124_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='originalstory',
            name='story_watchers',
            field=models.ManyToManyField(blank=True, related_name='watchers', to=settings.AUTH_USER_MODEL),
        ),
    ]
