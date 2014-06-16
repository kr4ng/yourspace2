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