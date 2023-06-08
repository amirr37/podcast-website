from django.db import models


# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(max_length=255, verbose_name='ایمیل')
    website = models.CharField(max_length=255, verbose_name='ویسایت', null=True)
    message = models.TextField( verbose_name='متن پیام')
    created_time = models.DateTimeField(auto_now_add=True)
    is_read_by_admin = models.BooleanField(default=False)

    def __str__(self): return f"{self.name} - {self.created_time.date}"

    class Meta:
        verbose_name='پیام تماس با ما'
        verbose_name_plural='لیست پیام های تماس با ما'


