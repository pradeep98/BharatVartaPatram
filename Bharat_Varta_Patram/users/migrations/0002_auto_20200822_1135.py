# Generated by Django 2.2.12 on 2020-08-22 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='Sonipat', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='occupation',
            field=models.CharField(default='SonipatStudent', max_length=20),
            preserve_default=False,
        ),
    ]
