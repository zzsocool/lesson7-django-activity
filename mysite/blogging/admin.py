from django.contrib import admin
from blogging.models import Post
from blogging.models import Category
admin.site.register(Category)
admin.site.register(Post)
# Register your models here.
