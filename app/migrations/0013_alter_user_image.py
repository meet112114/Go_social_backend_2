# Generated by Django 4.2.7 on 2024-03-20 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='profile_images/defaultprp.jpg', null=True, upload_to='profile_images/'),
        ),
    ]