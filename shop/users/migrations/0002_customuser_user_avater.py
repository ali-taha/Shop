# Generated by Django 4.0 on 2021-12-28 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_avater',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/user_avatar'),
        ),
    ]
