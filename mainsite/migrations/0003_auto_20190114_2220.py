# Generated by Django 2.1.4 on 2019-01-14 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_auto_20190114_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userstoryparagraphs',
            name='user_paragraph',
            field=models.TextField(max_length=1000),
        ),
    ]