# Generated by Django 3.2.13 on 2022-08-10 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('booking_reference', models.CharField(max_length=255)),
                ('num_guests', models.IntegerField()),
            ],
        ),
    ]
