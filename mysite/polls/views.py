from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# create requirements that request must include location of files and altitude
def index(request):
    #insert code to send images to image processing algorithm here
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    response  = "You're looking at question %s"
    return HttpResponse(response % question_id)

def results(request, question_id):
    response  = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)

def detail(request, question_id):
    response  = "You're voting on question %s"
    return HttpResponse(response % question_id)
