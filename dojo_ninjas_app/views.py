from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        'dojos' : Dojo.objects.all(),
    }
    return render(request, 'dojo_ninjas.html', context)

def dojos_create(request):
    Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
    return redirect('/')    

def ninjas_create(request):
    Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'],dojo = Dojo.objects.get(id=request.POST['dojo']))
    return redirect('/')  

# def delete_dojo(request, dojo_id):
#     dojo=Dojo.objects.get(pk=dojo_id)
#     dojo.delete()   
#     return render(request, 'dojo_ninjas.html')


