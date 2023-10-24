from django.http import HttpResponse
from django.template import loader

def login(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def register(request):
  template = loader.get_template('register.html')
  return HttpResponse(template.render())

def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def blogs(request):
  template = loader.get_template('blogs.html')
  return HttpResponse(template.render())