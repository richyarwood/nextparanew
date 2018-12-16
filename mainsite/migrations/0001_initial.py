# Generated by Django 2.1.4 on 2018-12-16 23:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OriginalStory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_headline', models.CharField(blank=True, max_length=500)),
                ('story_publish_date', models.DateTimeField(auto_now_add=True)),
                ('story_first_paragraph', models.TextField(blank=True, max_length=600)),
                ('slug', models.SlugField(max_length=250, null=True)),
                ('story_paragraph_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserStoryParagraphs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_paragraph', models.TextField(max_length=800)),
                ('user_paragraph_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Date added')),
                ('paragraph_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('story_belongs_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paragraphs', to='mainsite.OriginalStory')),
            ],
        ),
    ]
