# Generated by Django 2.0.2 on 2018-09-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venues', '0002_event_venue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='entry_end_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='entry_start_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_end_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='review_by_datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
