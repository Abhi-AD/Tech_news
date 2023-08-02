from django.contrib import admin
from news_app.models import Category,Tag,Post,Review

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Review)