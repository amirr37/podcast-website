# Generated by Django 4.0.6 on 2023-05-10 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(verbose_name='متن پیام'),
        ),
    ]
