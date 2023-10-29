from django.contrib import admin
from .models import Blog, Author, Entry

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'tagline')
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    
admin.site.register(Entry)