# Generated by Django 3.0.6 on 2020-05-18 14:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('music', '0003_auto_20200518_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
