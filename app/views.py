from django.shortcuts import render
from app.models import *

# Create your views here.
def abhi(request):
    a=Topic.objects.all()
    d={'Topic':a}

    return render(request,'Topic.html',context=d)



def damu(request):
    a=Webpage.objects.all()
    d={'web':a}

    return render(request,'Webpage.html',context=d)


def bheem(request):
    a=AcessRecord.objects.all()
    d={'AcessRecord':a}

    return render(request,'AcessRecord.html',context=d)

