# Generated by Django 2.0.2 on 2018-06-19 14:23

from django.db import migrations
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('musicians', '0014_auto_20180608_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='state',
            field=localflavor.us.models.USStateField(blank=True, max_length=2, null=True),
        ),
    ]