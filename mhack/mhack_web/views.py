from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
# Create your views here.

def login(request):
	t=get_template('login.html')
	c=Context()
	return HttpResponse(t.render(c))

def friends(request):
	t=get_template('friends.html')
	c=Context()
	return HttpResponse(t.render(c))