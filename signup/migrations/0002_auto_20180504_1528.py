# Generated by Django 2.0.5 on 2018-05-04 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.TextField(max_length=30, null=True),
        ),
    ]
