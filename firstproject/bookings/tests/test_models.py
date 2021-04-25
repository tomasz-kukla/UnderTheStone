import datetime
import pytz

from django.test import SimpleTestCase, TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError

from bookings.models import Reservation, Table, Section


class ReservationTestCase(TestCase):
    def setUp(self):
        self.section = Section.objects.create(name='Garden Down1')

        self.table1 = Table.objects.create(section=self.section, code='ABC')
        self.table2 = Table.objects.create(section=self.section, code='ABD')

    def test_reservation_creation(self):
        reservation = Reservation.objects.create(
            table=self.table1,
            start='2021-05-16T14:30',
            end='2021-05-16T16:30',
            firstname="Test1",
            lastname="Test1",
            email="test@gmail.com",
        )
        self.assertNotEquals(reservation, None)

    def test_reservation_start_in_past(self):
        with self.assertRaises(ValidationError):
            reservation = Reservation.objects.create(
                table=self.table1,
                start='2021-04-18T14:30',
                end='2021-04-18T16:30',
                firstname="Test1",
                lastname="Test1",
                email="test@gmail.com",
            )

    def test_reservation_end_in_past(self):
        with self.assertRaises(ValidationError):
            reservation = Reservation.objects.create(
                table=self.table1,
                start='2021-05-16T14:30',
                end='2021-05-14T16:30',
                firstname="Test1",
                lastname="Test1",
                email="test@gmail.com",
            )

    def test_reservation_start_end_in_past(self):
        with self.assertRaises(ValidationError):
            reservation = Reservation.objects.create(
                table=self.table1,
                start='2021-04-10T14:30',
                end='2021-04-10T16:30',
                firstname="Test1",
                lastname="Test1",
                email="test@gmail.com",
            )

    def test_reservation_before_opening_hour(self):
        with self.assertRaises(ValidationError):
            reservation = Reservation.objects.create(
                table=self.table1,
                start='2021-04-16T8:30',
                end='2021-04-16T9:30',
                firstname="Test1",
                lastname="Test1",
                email="test@gmail.com",
            )

    def test_reservation_start_before_opening_hour(self):
        with self.assertRaises(ValidationError):
            reservation = Reservation.objects.create(
                table=self.table1,
                start='2021-04-16T8:30',
                end='2021-04-16T10:30',
                firstname="Test1",
                lastname="Test1",
                email="test@gmail.com",
            )

    def test_reservation_end_before_opening_hour(self):
        with self.assertRaises(ValidationError):
            reservation = Reservation.objects.create(
                table=self.table1,
                start='2021-04-16T10:30',
                end='2021-04-16T9:30',
                firstname="Test1",
                lastname="Test1",
                email="test@gmail.com",
            )

    def test_reservation_after_opening_hour(self):
        with self.assertRaises(ValidationError):
            reservation = Reservation.objects.create(
                table=self.table1,
                start='2021-04-15T23:30',
                end='2021-04-16T1:30',
                firstname="Test1",
                lastname="Test1",
                email="test@gmail.com",
            )

    def test_reservation_shorter_than_30_minutes(self):
        with self.assertRaises(ValidationError):
            reservation = Reservation.objects.create(
                table=self.table1,
                start='2021-04-16T14:30',
                end='2021-04-16T14:52',
                firstname="Test1",
                lastname="Test1",
                email="test@gmail.com",
            )

    def test_reservation_longer_than_4_hours(self):
        with self.assertRaises(ValidationError):
            reservation = Reservation.objects.create(
                table=self.table1,
                start='2021-04-16T14:30',
                end='2021-04-16T19:01',
                firstname="Test1",
                lastname="Test1",
                email="test@gmail.com",
            )

    def test_reservation_on_already_taken_table(self):
        with self.assertRaises(ValidationError):
            reservation1 = Reservation.objects.create(
                table=self.table1,
                start='2021-04-16T14:30',
                end='2021-04-16T15:30',
                firstname="Test1",
                lastname="Test1",
                email="test@gmail.com",
            )
            reservation2 = Reservation.objects.create(
                table=self.table1,
                start='2021-04-16T14:30',
                end='2021-04-16T15:30',
                firstname="Test1",
                lastname="Test1",
                email="test@gmail.com",
            )

    def test_reservation_on_different_table_at_the_same_time(self):
        reservation1 = Reservation.objects.create(
            table=self.table1,
            start='2021-05-16T14:30',
            end='2021-05-16T15:30',
            firstname="Test1",
            lastname="Test1",
            email="test@gmail.com",
        )
        reservation2 = Reservation.objects.create(
            table=self.table2,
            start='2021-05-16T14:30',
            end='2021-05-16T15:30',
            firstname="Test2",
            lastname="Test2",
            email="test@gmail.com",
        )
        self.assertEquals(Reservation.objects.all().count(), 2)
