from django import http
from django.shortcuts import render

# Create your views here.
"""
# FBV:
1. Function that has one or more params;
2. Returns a response
"""


def index(request):
    return http.HttpResponse('It works')
