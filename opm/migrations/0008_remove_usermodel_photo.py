# Generated by Django 3.0.7 on 2020-08-16 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opm', '0007_usermodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='photo',
        ),
    ]
