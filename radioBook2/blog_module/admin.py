from django.contrib import admin
from blog_module.models import Blog, Category


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'read_time', ]
    list_editable = ['slug', 'category', 'read_time', ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'parent', ]
    list_editable = [ 'slug', 'parent']


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

