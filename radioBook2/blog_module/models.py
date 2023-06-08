from django.db import models
from jalali_date import date2jalali

from podcast_module.models import Tag


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان دسته بندی')
    slug = models.SlugField(max_length=255, default="", null=False, unique=True)
    parent = models.ForeignKey(to='Category', verbose_name='دسته بندی والد', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    short_description = models.TextField(verbose_name='توضیح کوتاه', max_length=200)
    author = models.CharField(max_length=255, verbose_name='نویسنده')
    avatar = models.ImageField(upload_to='images/blog_avatars', verbose_name='آوارتار بلاگ')
    background_image = models.ImageField(upload_to='images/blog_backgrounds', verbose_name='تصویر بکگراند')
    slug = models.SlugField(max_length=255, default="", null=False, unique=True)
    category = models.ForeignKey(Category, verbose_name='دسته بندی', null=True, on_delete=models.CASCADE,
                                 related_name='blog')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    text_content = models.TextField(verbose_name='متن مقاله')
    read_time = models.IntegerField(verbose_name='زمان تخمینی مطالعه', default=5)
    tags = models.ManyToManyField(to=Tag, related_name='blog', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'بلاگ'
        verbose_name = 'مقاله'

    def get_jalali_created_date(self):
        return date2jalali(self.created_time)
