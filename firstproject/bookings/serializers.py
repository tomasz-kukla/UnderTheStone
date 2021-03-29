from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Section, Table, Reservation
# it will convert the class objects into .json datatypes


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = ('id', 'name', 'ground_level', 'allowed_smoking')


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    reservations = ReservationSerializer(many=True)

    class Meta:
        model = Table
        fields = ('id', 'number_of_seats', 'code')
