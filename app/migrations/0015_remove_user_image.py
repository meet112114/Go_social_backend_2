# Generated by Django 4.2.7 on 2024-03-22 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_co_ee_ej_if_me_remove_userfollow_follows_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]
