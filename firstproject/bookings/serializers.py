from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from .models import Section, Table, Reservation
# it will convert the class objects into .json datatypes


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'


class TableSerializer(serializers.ModelSerializer):
    reservations = ReservationSerializer(many=True)

    class Meta:
        model = Table
        fields = '__all__'
