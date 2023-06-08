from django.shortcuts import render
from django.views.generic import FormView
from contact_module.forms import ContactUsModelForm


# Create your views here.


class ContactUsView(FormView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
