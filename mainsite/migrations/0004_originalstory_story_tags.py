# Generated by Django 2.1.4 on 2019-01-06 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0001_initial'),
        ('mainsite', '0003_auto_20190104_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='originalstory',
            name='story_tags',
            field=models.ManyToManyField(to='tagging.StoryTags'),
        ),
    ]
