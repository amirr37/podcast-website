# Generated by Django 4.0.6 on 2023-04-30 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0003_category_blog_tags_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog_module.category', verbose_name='دسته بندی والد'),
        ),
    ]
