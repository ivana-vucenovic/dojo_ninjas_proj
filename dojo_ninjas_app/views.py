from django.shortcuts import render

def index(request):
    return render(request, 'dojo_ninjas.html')
# Create your views here.
