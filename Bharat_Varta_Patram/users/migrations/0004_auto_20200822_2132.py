# Generated by Django 2.2.12 on 2020-08-22 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200822_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
