from django.contrib import admin
from .models import Category, Subcategory, Subject, Video,Snippet
# Register your models here.
admin.site.register(Category)
admin.site.register(Subject)
admin.site.register(Subcategory)
admin.site.register(Video)
admin.site.register(Snippet)
