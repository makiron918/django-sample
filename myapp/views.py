from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
  return render(request,'index.html')

def welcome(request): # welcome関数
	return render(request, 'welcome.html') # welcome.htmlを返す

def like(request): # like関数
  return render(request,'like.html') # like.htmlを返す

def dislike(request): # dislike関数
  return render(request,'dislike.html') # dislike.htmlを返す

def birthday(request): # birthday関数
  return render(request,'birthday.html') # birthday.htmlを返す
