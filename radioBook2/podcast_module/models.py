import datetime

import django.utils.timezone
from django.conf import settings
from django.utils.text import slugify
from django.db import models
from django_quill.fields import QuillField
from jalali_date import date2jalali


# Create your models here.

class Season(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان فصل')
    number = models.IntegerField(verbose_name='شماره فصل')
    description = models.TextField(verbose_name='توضیحات فصل', null=False, default="")
    background_image = models.ImageField(verbose_name='تصویر بکگراند', upload_to='images/backgrounds')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'فصل'
        verbose_name_plural = 'لیست فصل ها'


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'لیست تگ ها'
        verbose_name = 'تگ'


class Podcast(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name='عنوان')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, db_index=True)
    main_episode = models.IntegerField(default=1, )
    season_episode = models.IntegerField(verbose_name='شماره قسمت فصل', null=False, default=1)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    producer = models.CharField(max_length=255, verbose_name='تهیه کننده')
    short_description = models.TextField(verbose_name='توضیحات کوتاه', null=False, default="")
    content = QuillField(null=True)
    avatar = models.ImageField(verbose_name='تصویر پادکست', upload_to='images/avatars')
    background_image = models.ImageField(verbose_name='تصویر بکگراند', upload_to='images/backgrounds')
    podcast_file = models.FileField(verbose_name='فایل پادکست', upload_to='podcast_files')
    tags = models.ManyToManyField(to=Tag, related_name='tags')
    slug = models.SlugField(max_length=255, default="", null=False, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'پادکست ها'
        verbose_name = 'پادکست'

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def get_jalali_created_date(self):
        return date2jalali(self.created_time)

# class QuillPost(models.Model):


# class Comment(models.Model):
#     pass
