# Generated by Django 2.2.13 on 2020-06-14 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='url',
            new_name='video_url',
        ),
    ]
