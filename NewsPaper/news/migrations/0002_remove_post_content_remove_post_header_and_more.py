# Generated by Django 4.1.4 on 2022-12-25 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='header',
        ),
        migrations.AddField(
            model_name='author',
            name='ratingPost',
            field=models.SmallIntegerField(default=0),
        ),
    ]
