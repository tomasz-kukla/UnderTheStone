# Generated by Django 3.1.7 on 2021-04-25 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_auto_20210425_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='reservation_code',
            new_name='code',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='customer_email',
            new_name='email',
        ),
    ]
