from enum import auto
from django.db import models
from django.db.models.base import Model
from django.db.models.expressions import F
from django.urls import reverse
from tinymce.models import HTMLField


# Create your models here.
class hsnc(models.Model):
    category = models.CharField(max_length=50,default="")
    slug = models.SlugField(max_length=50)
    class Meta:
        verbose_name_plural ="HSNC _Data"
    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse("hemophilia:hemophilia", args=[self.slug])

class posts(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(hsnc, on_delete=models.CASCADE)
    title = models.CharField(max_length=100,default="")
    content = HTMLField()
    slug = models.SlugField(max_length=50)
    image_1 = models.FileField(upload_to="images",null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("hemophilia:about", args=[self.slug])

class TreatMents(models.Model):
    title = models.CharField(max_length=100, null=False)
    content = HTMLField(default="")

    slug = models.SlugField(max_length=50, default="")
    image_1 = models.FileField(upload_to="images",null=True, blank=True)
    image_2 = models.FileField(upload_to="images",null=True, blank=True)
    image_3 = models.FileField(upload_to="images",null=True, blank=True)

    class Meta:
        verbose_name_plural ="Treatments"
    def __str__(self):
        return self.title

class ContactUs(models.Model):
    name = models.CharField(max_length=100, null=False,blank=False)
    email = models.EmailField(blank=False,null=False,max_length=254)
    mo_no = models.IntegerField(blank=True, null=True)
    query = models.TextField(blank=False,null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural ="Contact Us"


class RealStories(models.Model):
    heading = models.CharField(max_length=150,blank=False, null=False,default="Real Story")
    description = models.TextField(blank=False,null=False)
    image = models.FileField(upload_to="realstory", null=True, blank=True)

    def __str__(self):
        return self.heading
    
    class Meta:
        verbose_name_plural ="Real Stories"

class Slider(models.Model):
    heading = models.CharField(max_length=150,blank=False, null=False,default=" ")
    description = models.TextField(blank=False,null=False)
    image = models.FileField(upload_to="slider", null=True, blank=True)

    def __str__(self):
        return self.heading
    
    class Meta:
        verbose_name_plural ="Slider"
