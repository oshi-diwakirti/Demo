from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('', admin.site.urls),
    path('partners/', include('partners.urls')),
    path('publish/', include('publish.urls')),
]
