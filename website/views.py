from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from website.models import Person
# Create your views here.
def home(request):
    names = Person.objects.all()
    template = loader.get_template('website/index.html')
    context = RequestContext(request, {
        'names': names,
    })
    return HttpResponse(template.render(context))

def about(request):
    names = Person.objects.all()
    template = loader.get_template('website/about.html')
    context = RequestContext(request, {
        'names': names,
    })
    return HttpResponse(template.render(context))

def photos(request):
    names = Person.objects.all()
    template = loader.get_template('website/photos.html')
    context = RequestContext(request, {
        'names': names,
    })
    return HttpResponse(template.render(context))

def pricing(request):
    names = Person.objects.all()
    template = loader.get_template('website/pricing.html')
    context = RequestContext(request, {
        'names': names,
    })
    return HttpResponse(template.render(context))

def contact(request):
    names = Person.objects.all()
    template = loader.get_template('website/contact.html')
    context = RequestContext(request, {
        'names': names,
    })
    return HttpResponse(template.render(context))

def reserve(request):
    names = Person.objects.all()
    template = loader.get_template('website/reserve.html')
    context = RequestContext(request, {
        'names': names,
    })
    return HttpResponse(template.render(context))