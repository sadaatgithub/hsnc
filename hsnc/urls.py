
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('home.urls')),
    path('hemophilia/', include('hemophilia.urls')),
    path('vWd/', include('vwd.urls')),
    # path('women-bleeders/', include('home.urls')),
    # path('treatments/', include('home.urls')),
    # path('inhibitors/', include('home.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
