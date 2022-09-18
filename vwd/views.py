from django.shortcuts import render

from home.models import hsnc, posts
from .models import VWD

# Create your views here.
def vWd(request):
    str = 'von-willebrand-disease'
    category = hsnc.objects.get(slug=str)
    qs = posts.objects.all().filter(category=category).exclude(slug='von-willebrand-disease')
    query = posts.objects.all().filter(category=category).filter(slug='von-willebrand-disease')
    status = True
    context = {'query':query,'qs':qs,'bd':status}
    return render(request,'vWd/index.html',context)



def vWd_more(request, slug):
    qs = VWD.objects.all().exclude(slug = slug)
    query = VWD.objects.filter(slug = slug)
    status = True
    context = {'query':query,'qs':qs,'bd':status}
    return render(request,'vWd/index.html',context)