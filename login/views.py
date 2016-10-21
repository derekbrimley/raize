from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello World")

def results(request, question_id):
	return HttpResponse("you put in a number")