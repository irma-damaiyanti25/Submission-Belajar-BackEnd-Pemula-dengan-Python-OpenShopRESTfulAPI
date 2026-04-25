from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # ambil routing dari app OpenShop
    path('', include('OpenShop.urls')),
]