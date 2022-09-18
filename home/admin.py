from home.views import treatments
from django.contrib import admin
from .models import ContactUs, RealStories, hsnc,TreatMents,Slider, posts

# Register your models here.
admin.site.register(hsnc)
admin.site.register(TreatMents)
admin.site.register(ContactUs)
admin.site.register(RealStories)
admin.site.register(Slider)
admin.site.register(posts)