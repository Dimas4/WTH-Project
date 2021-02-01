from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('wth_base.urls')),
    path('admin/', admin.site.urls),
]
