# Generated by Django 2.0.2 on 2018-06-08 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicians', '0013_musicianvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musicianaudio',
            name='musician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audios', to='musicians.Musician'),
        ),
        migrations.AlterField(
            model_name='musicianvideo',
            name='musician',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='musicians.Musician'),
        ),
    ]
