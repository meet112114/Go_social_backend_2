# Generated by Django 4.2.7 on 2024-03-22 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_alter_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=64)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=64)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='EJ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=64)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='IF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=64)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ME',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=64)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='userfollow',
            name='follows',
        ),
        migrations.RemoveField(
            model_name='userfollow',
            name='user',
        ),
        migrations.DeleteModel(
            name='PostComment',
        ),
        migrations.DeleteModel(
            name='UserFollow',
        ),
    ]