from django.db import reset_queries
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import hsnc, TreatMents, ContactUs,RealStories, Slider, posts
from hemophilia.models import Hemophilia
# Create your views here.


def categories(request):
    return{'categories':hsnc.objects.all()}

def index(request):
    status =True
    qs = RealStories.objects.all()
    slider = Slider.objects.all()
    context = {'qs':qs,'home':status, 'slider':slider}
    return render(request, 'home/index.html', context)

def inhibitors(request):
    # qs = Hemophilia.objects.all().exclude(slug=slug)
    query = posts.objects.filter(slug='inhibitors')
    status = True
    context = {'query':query,'bd':status}
    return render(request, 'hemophilia/hemophilia.html',context)

def treatments(request):
    category = hsnc.objects.get(slug="treatments")
    qs = posts.objects.all().filter(category=category)
    status =True
    context = {'qs':qs, 'bd':status}
    return render(request, 'home/treatments.html', context)

def treatmentsDetails(request,slug,category):
    post_category = hsnc.objects.get(category=category)
    qs = posts.objects.filter(category=post_category).exclude(slug=slug)
    query = posts.objects.filter(slug=slug)
    # qs = posts.objects.all().exclude(slug=slug)
    # query = posts.objects.filter(slug=slug)
    status = True
    context = {'query':query,'qs':qs,'bd':status}
    return render(request, 'home/treatments.html', context)

def womenBleeders(request):
    query = posts.objects.filter(slug='women-with-bleeding-disorder')

    status = True
    context = {'bd':status,'query':query}
    return render(request, 'hemophilia/womenBleeders.html', context)

def contactUs(request):
    status = True

    if request.method =='POST':
            name = request.POST['name']
            email = request.POST['email']
            mo_no = request.POST['contact_no']
            msg = request.POST['content']
            msgData = ContactUs()
            msgData.name = name
            msgData.email = email
            msgData.mo_no = mo_no
            msgData.query = msg
            msgData.save()
            return render(request, 'home/contactUs.html')
    context = {'status':status}
    return render(request, 'home/contactUs.html',context)


def realstories(request, pk):
    qs = RealStories.objects.all().filter(pk=pk)
    context = {'qs':qs}
    return render(request, 'home/realstories.html', context)