# Generated by Django 2.0.2 on 2018-07-17 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicians', '0019_musicianphoto'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MusicianPhoto',
            new_name='MusicianImage',
        ),
    ]
