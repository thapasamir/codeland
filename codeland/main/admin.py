from django.contrib import admin
from .import models
# Register your models here.

admin.site.register(models.section)



@admin.register(models.cateogies)
class CateogiesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}