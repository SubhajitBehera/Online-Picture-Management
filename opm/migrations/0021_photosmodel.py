# Generated by Django 3.0.7 on 2020-08-18 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opm', '0020_delete_photosmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotosModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='photos/')),
                ('captions', models.TextField()),
                ('videos', models.FileField(null=True, upload_to='videos/', verbose_name='')),
            ],
        ),
    ]
