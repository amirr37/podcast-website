# Generated by Django 4.0.6 on 2023-04-30 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='read_time',
            field=models.IntegerField(default=5, verbose_name='زمان تخمینی مطالعه'),
        ),
    ]
