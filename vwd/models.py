from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class VWD(models.Model):
    title= models.CharField(max_length=100, null=False)
    content =HTMLField(default="")
    slug = models.SlugField(default="")
    image_1 = models.FileField(upload_to="images",null=True, blank=True)
    image_2 = models.FileField(upload_to="images",null=True, blank=True)
    image_3 = models.FileField(upload_to="images",null=True, blank=True)
    # treatment = models.OneToOneField(Treatment,)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural ="von Willebrand Disease"