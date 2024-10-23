from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def coffee(request):
	return HttpResponse("Hi, Blog!")