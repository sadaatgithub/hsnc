from django.shortcuts import render,get_object_or_404
from home.models import hsnc, posts
from django.contrib.sites.shortcuts import get_current_site


# Create your views here.
def hemophilia(request):
    category = hsnc.objects.get(slug__icontains='Hemophilia')
    qs = posts.objects.all().filter(category=category).exclude(slug='what-is-hemophilia')
    query = posts.objects.all().filter(category=category).filter(slug='what-is-hemophilia')
        # query = posts.objects.all().filter(category=category).filter(slug='von-willebrand-disease')

    status = True
    context = {'query':query,'qs':qs,'bd':status}
    return render(request,'hemophilia/hemophilia.html',context)

def about(request, slug,category):
    post_category = hsnc.objects.get(category=category)
    qs = posts.objects.filter(category=post_category).exclude(slug=slug)
    query = posts.objects.filter(slug=slug)
    status = True
    context = {'query':query,'qs':qs,'bd':status}
    return render(request, 'hemophilia/hemophilia.html',context)

