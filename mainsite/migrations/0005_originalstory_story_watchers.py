# Generated by Django 2.1.4 on 2019-01-24 20:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainsite', '0004_remove_originalstory_story_watchers'),
    ]

    operations = [
        migrations.AddField(
            model_name='originalstory',
            name='story_watchers',
            field=models.ManyToManyField(blank=True, null=True, related_name='watchhers', to=settings.AUTH_USER_MODEL),
        ),
    ]
