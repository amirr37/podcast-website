from django.urls import path
from about_module import views

urlpatterns = [
    path('', views.AboutUsView.as_view(), name='about_us_page')
]
