# Generated by Django 4.0.6 on 2023-04-30 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_module', '0004_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blog_module.category', verbose_name='دسته بندی'),
        ),
    ]
