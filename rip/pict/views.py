from django.shortcuts import render
from .models import *
from django.forms.models import model_to_dict

def index(request):
    pictures = None
    delId = int( request.POST.get('delId', 0) if request.POST.get('delId', 0) != '' else 0 )
    count = int( request.POST.get('count', 0) if request.POST.get('count', 0) != '' else 0 )
    if delId:
        try:
            picts = list( Pictures.objects.all() )
            picts[delId - 1].delete()
        except IndexError:
            pass
    if count:
        pictures = list( Pictures.objects.all() )[:count]
    else:
        pictures = list( Pictures.objects.all() )
    return render(request, 'menu.html', { 'pictures' : pictures })

def item(request, id):
    instance = Pictures.objects.get(pk=id)
    picture = model_to_dict(instance, fields=[field.name for field in instance._meta.fields])
    return render(request, 'item.html', picture)

