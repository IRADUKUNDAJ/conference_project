from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html',context)  

def createconference(request):
    context = {}
    return render(request, 'createconference.html',context) 

