# Generated by Django 4.2.7 on 2024-04-07 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_rename_lectures_lecturesif'),
    ]

    operations = [
        migrations.CreateModel(
            name='LecturesCO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('link', models.CharField(max_length=64)),
                ('time', models.CharField(default='7:00 AM', max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='LecturesEE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('link', models.CharField(max_length=64)),
                ('time', models.CharField(default='7:00 AM', max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='LecturesEJ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('link', models.CharField(max_length=64)),
                ('time', models.CharField(default='7:00 AM', max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='LecturesME',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('link', models.CharField(max_length=64)),
                ('time', models.CharField(default='7:00 AM', max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
    ]