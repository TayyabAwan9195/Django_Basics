# Generated by Django 5.0.6 on 2024-07-15 09:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_receipe_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['department'],
            },
        ),
        migrations.CreateModel(
            name='StudentID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=100)),
                ('student_email', models.EmailField(max_length=254, unique=True)),
                ('student_age', models.IntegerField(default=18)),
                ('student_address', models.TextField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='depart', to='vege.department')),
                ('student_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='studentid', to='vege.studentid')),
            ],
            options={
                'verbose_name': 'student',
                'ordering': ['student_name'],
            },
        ),
    ]
