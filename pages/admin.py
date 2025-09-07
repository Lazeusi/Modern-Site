from django.contrib import admin
from .models import SlideImges
# Register your models here.

@admin.register(SlideImges)
class SlideImgesAdmin(admin.ModelAdmin):
    list_display = ['image' , 'title']