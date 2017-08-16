from django.contrib import admin
from blog.models import Type, Post, Image
# Register your models here.
admin.site.register(Type)
admin.site.register(Post)
admin.site.register(Image)
