# Generated by Django 3.0.7 on 2020-08-16 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opm', '0009_delete_usermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40, unique=True)),
                ('contactno', models.IntegerField(unique=True)),
                ('ps', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('photo', models.FileField(upload_to='documents/')),
                ('caption', models.TextField()),
            ],
        ),
    ]
