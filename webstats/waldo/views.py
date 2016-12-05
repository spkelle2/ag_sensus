from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from .models import player

def index(request):
    template = loader.get_template('waldo/index.html')
    context = {
            }
    return HttpResponse(template.render(context, request))

def validate(request):
    template = loader.get_template('waldo/validate.html')

    for key in request.POST:
        if request.POST[key] == '':
            context = {
                    }
            return HttpResponse(template.render(context, request))

    current_player = player()
    current_player.first_name = request.POST['first_name']
    current_player.last_name = request.POST['last_name']
    current_player.gender = request.POST['gender']
    current_player.age = request.POST['age']
    current_player.save()

    # create a session
    request.session['id'] = current_player.id

    return HttpResponseRedirect(reverse('waldo:game'))

def game(request):
    current_player = player.objects.get(pk=request.session['id'])
    current_player.start_time = timezone.now

    template = loader.get_template('waldo/game.html')
    context = {
            }

    return HttpResponse(template.render(context, request))

def thanks(request):
    return HttpResponse("Thank you for playing!")
# Create your views here.
