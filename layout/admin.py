from django.contrib import admin
from . models import Person, Post, Follow_People

# Register your models here.
admin.site.register(Person)
admin.site.register(Post)
admin.site.register(Follow_People)