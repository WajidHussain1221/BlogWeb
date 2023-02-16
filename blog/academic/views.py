from django.shortcuts import render
from django.http import  HttpResponse
from . import  models
# Create your views here.


def index(request):
    subjects =  models.Subject.objects.all()
    return render(request,  "home.html" , {"subjects": subjects})

def downloads(request, id):
    papers = models.Paper.objects.filter(id=id)
    return  render(request, "downloads.html", {"academic": papers})