# Generated by Django 3.0.7 on 2020-08-18 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opm', '0017_photosmodel_usermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='photosmodel',
            name='videos',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]
