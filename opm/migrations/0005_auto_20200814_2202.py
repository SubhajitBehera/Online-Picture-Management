# Generated by Django 3.0.7 on 2020-08-14 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opm', '0004_auto_20200814_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(max_length=40),
        ),
    ]