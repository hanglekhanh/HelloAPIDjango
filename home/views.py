# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})


@api_view(['GET', 'POST'])
def calculate(request,a,b):
    i = int(a);
    t = int(b);
    if request.method == 'POST':
        return Response(i+t)
    return Response(i+t)

