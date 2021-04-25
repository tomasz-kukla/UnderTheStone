# Generated by Django 3.1.7 on 2021-04-25 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='annotation',
            field=models.TextField(blank=True, default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='firstname',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='lastname',
            field=models.CharField(max_length=40),
        ),
    ]
