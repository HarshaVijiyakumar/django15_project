from django.contrib import admin

# Register your models here.

from .models import PostGroup, PostGroup2

admin.site.register(PostGroup)
admin.site.register(PostGroup2)
