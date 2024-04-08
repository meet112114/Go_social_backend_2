# Generated by Django 4.2.7 on 2024-04-08 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_sports'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('enrollmentId', models.IntegerField()),
                ('yearAndDept', models.CharField(max_length=16)),
                ('Complaint', models.CharField(max_length=164)),
            ],
        ),
    ]
