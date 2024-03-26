from django.contrib import admin
from .models import ConexionDB



class ConexionDBAdmin(admin.ModelAdmin):
    list_display = ("name", "host", "user")
    search_fields = ("name", "host")


admin.site.register(ConexionDB, ConexionDBAdmin)

