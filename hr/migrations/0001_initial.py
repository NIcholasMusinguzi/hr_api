# Generated by Django 5.1.1 on 2024-10-05 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('other_names', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('id_photo', models.ImageField(blank=True, null=True, upload_to='photos/')),
                ('employee_number', models.CharField(max_length=10, unique=True)),
            ],
        ),
    ]
