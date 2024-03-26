from django.contrib import admin
from django.urls import path

from report import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dash/', views.index, name="dash"),
]
