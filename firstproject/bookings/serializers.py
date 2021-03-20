from rest_framework import serializers
from .models import Section, Table, Reservation, Type
# it will convert the class objects into json datatypes


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('section_id', 'name', 'ground_level', 'allowed_smoking')


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('table_id', 'number_of_seats')


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('reservation_id', 'reservation_start',
                  'reservation_end', 'customer_surname', "reservation_code")


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('type_id', 'name', 'special_annotation')