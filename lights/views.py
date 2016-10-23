from django.shortcuts import render
from django.http import HttpResponse
from .models import LightButton
from django.template import loader

def index(request):
	
	buttons = LightButton.objects.all()
	template = loader.get_template('lights/index.html')
	
	context = {'buttons':buttons,
	}	
	
	return HttpResponse (template.render(context, request))
