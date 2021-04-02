
from rest_framework import viewsets
from django.db.models import fields, query
from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializers import ReservationSerializer
from .models import Reservation
from rest_framework.response import Response
from rest_framework import status, generics


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer()

    @api_view(['GET', 'POST'])
    def reservation_list(request, format=None):

        if request.method == 'GET':
            reservations = Reservation.objects.all()
            serializer = ReservationSerializer(reservations, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = ReservationSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)