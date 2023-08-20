from django.shortcuts import render
from django.template import loader
from .models import Person
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
def member(request):
    mymembers = Person.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request,id):
    mymember=Person.objects.get(id=id)
    template=loader.get_template('details.html')
    context={
        'mymember': mymember,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template=loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mymembers=Person.objects.all().order_by('firstname').values()
    template=loader.get_template('template.html')
    context={
        'fruits':['Apple','Banana','cherry'],
        'firstname':'Deepak',
        'mymembers': mymembers,
        'x':['csa','csb','csc'],
        'y':['csa','csb','csc']
    }
    return HttpResponse(template.render(context,request))