from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class AboutUsView(TemplateView):
    template_name = 'about_module/about_us_page.html'
