# Generated by Django 5.1.2 on 2024-10-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='avatar.png', upload_to='profile_pics'),
        ),
    ]