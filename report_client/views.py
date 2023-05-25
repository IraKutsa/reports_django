from django.shortcuts import render
from rest_framework import generics

from report_client import serializers


# Create your views here.
class ReportsView(generics.CreateAPIView):
    serializer_class = serializers.ReportSerializer

