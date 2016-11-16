from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# create requirements that request must include location of files and altitude
def index(request):
    #insert code to send images to image processing algorithm here
    return HttpResponse("Hello, world. You're at the polls index.")
