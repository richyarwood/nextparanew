# Generated by Django 2.1.4 on 2018-12-28 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorprofile',
            name='author_image',
            field=models.ImageField(upload_to='mains˙ite/static/images/'),
        ),
    ]
