from django.urls import path
from blog_module import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list_page'),
    path('/<category>/<slug:slug>', views.BlogDetailView.as_view(), name='blog_detail_page'),
    path('/category/<str:category>', views.category_view, name='category_page')
]
