from django.db import models
from django.db.models.fields import AutoField, TextField
import string
import random


def generate_reservation_code():
    lenght = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, l=lenght))
        if Reservation.objects.filter(reservation_code=code).count() == 0:
            break
    return code
# Create your models here.


class Section(models.Model):
    section_id = models.IntegerField(
        primary_key=True, unique=True)
    name = models.CharField(max_length=20, default='---', unique=True)
    ground_level = models.IntegerField(max_length=2, default=0)
    allowed_smoking = models.BooleanField(default=False)


class Table(models.Model):
    table_id = models.TextField(primary_key=True, unique=True)
    number_of_seats = models.IntegerField(default=1)


class Reservation(models.Model):
    reservation_id = models.IntegerField(
        primary_key=True, unique=True)
    reservation_start = models.DateTimeField(
        auto_now=False, auto_now_add=False)
    reservation_end = models.DateTimeField(
        auto_now=False, auto_now_add=False)
    customer_surname = models.TextField(max_length=40)
    reservation_code = models.CharField(max_length=9, default="", unique=True)


class Type(models.Model):
    type_id = models.IntegerField(
        primary_key=True, unique=True)
    name = models.CharField(max_length=20, default='---', unique=True)
    special_annotation = models.CharField(max_length=254, default='')
