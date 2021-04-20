import string
import random

from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields import AutoField, TextField

from django.db import models


def generate_reservation_code():
    lenght = 7

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=lenght))
        if Reservation.objects.filter(reservation_code=code).count() == 0:
            break
    return code


class Table(models.Model):
    number_of_seats = models.IntegerField(default=1)
    code = models.CharField(max_length=3, unique=True)

    def __str__(self) -> str:
        return f'Table {self.code} - {self.number_of_seats} seats'


class Section(models.Model):
    table = models.ForeignKey(Table, related_name='tables', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    floor = models.IntegerField(default=0)
    smoking_allowed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Section {self.name}'


class Reservation(models.Model):

    RESERVATION_CATEGORY = (
        ('Casual', 'Casual'),
        ('Birthday', 'Birthday'),
        ('Anniversary', 'Anniversary'),
        ('Other', 'Other'),
    )

    table = models.ForeignKey(
        Table, related_name='reservations', on_delete=PROTECT)

    start = models.DateTimeField()
    end = models.DateTimeField()
    reservation_code = models.CharField(max_length=9, default=generate_reservation_code, unique=True)

    firstname = models.TextField(max_length=40)
    lastname = models.TextField(max_length=40)
    customer_email = models.EmailField(max_length=254)

    category = models.CharField(blank=True, max_length=15, choices=RESERVATION_CATEGORY)
    annotation = models.CharField(blank=True, max_length=254, default='')

    def __str__(self) -> str:
        return f'{self.reservation_date} {self.name}'

    @property
    def name(self):
        return f'{self.firstname} {self.lastname}'
