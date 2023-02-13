from django.contrib import admin
from .models import Semester
# Register your models here.

class SemeseterAdmin(admin.ModelAdmin):
    search_fields = ['table']

admin.site.register(Semester, SemeseterAdmin)