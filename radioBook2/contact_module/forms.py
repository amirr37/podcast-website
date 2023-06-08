from django import forms
from .models import ContactUs
from django.utils.translation import gettext_lazy as _


class ContactUsModelForm(forms.ModelForm):
    # name = forms.CharField(error_messages={'required': 'لطفا نام و نام خانوادگی خود را وارد کنید'})
    # email = forms.CharField(error_messages={'required': 'لطفا ایمیل خود را وارد کنید'})
    # message = forms.CharField(error_messages={'required': 'لطفا متن پیام خود را وارد کنید'})

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'message']

        error_messages = {
            "name": {
                "required": _("لطفا نام و نام خانوادگی خود را وارد کنید"),
                'max_length': _("نام و نام خانوادگی نمی تواند بیشتر از ۲۵۵ کاراکتر باشد")
            }, "email": {
                "required": _("لطفا ایمیل خود را وارد کنید"),
                'max_length': _("ایمیل نمی تواند بیشتر از ۲۵۵ کاراکتر باشد")

            },
            "message": {
                "required": _("لطفا متن پیام خود را وارد کنید"),
            },
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'نام و نام خانوادگی',
                }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'ایمیل'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'متن پیام'
            })
        }
