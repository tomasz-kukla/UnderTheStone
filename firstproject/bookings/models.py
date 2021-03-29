from django.db import models
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import AutoField, TextField
import string
import random


def generate_reservation_code():
    lenght = 7

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=lenght))
        if Reservation.objects.filter(reservation_code=code).count() == 0:
            break
    return code


class Table(models.Model):
    number_of_seats = models.IntegerField(default=1)
    code = models.CharField(
        max_length=3, default='', unique=True)


class Section(models.Model):
    table = models.ForeignKey(
        Table, related_name='sections', on_delete=CASCADE)
    name = models.CharField(max_length=20, default='---', unique=True)
    ground_level = models.IntegerField(default=0)
    allowed_smoking = models.BooleanField(default=False)


class Reservation(models.Model):

    RESERVATION_TYPE = (
        ('Casual', 'Casual'),
        ('Birthday', 'Birthday'),
        ('Anniversary', 'Anniversary'),
        ('Other', 'Other'),
    )

    table = models.ForeignKey(Table, related_name='reservations', on_delete=PROTECT)

    reservation_date = models.DateField(auto_now=False, auto_now_add=False)
    reservation_start = models.TimeField(
        auto_created=False, auto_now=False, auto_now_add=False)
    reservation_end = models.TimeField(
        auto_created=False, auto_now=False, auto_now_add=False)
    reservation_code = models.CharField(
        max_length=9, default=generate_reservation_code, unique=True)
    reservation_type = models.CharField(
        max_length=15, choices=RESERVATION_TYPE)

    customer_firstname = models.TextField(max_length=40)
    customer_lastname = models.TextField(max_length=40)
    customer_email = models.EmailField(max_length=254)

    special_annotation = models.CharField(max_length=254, default='')
