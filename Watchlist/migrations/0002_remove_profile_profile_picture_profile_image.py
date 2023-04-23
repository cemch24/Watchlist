# Generated by Django 4.1.6 on 2023-04-19 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Watchlist', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
