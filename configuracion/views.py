from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
	return render(request, 'configuracion/index.html', {})