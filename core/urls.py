from django.contrib import admin
from django.urls import path
from app.views import list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list)
]
