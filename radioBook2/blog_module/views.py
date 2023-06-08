import jalali_date
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog_module.models import Blog, Category
from jalali_date import date2jalali, datetime2jalali

from podcast_module.models import Podcast


# Create your views here.

class BlogListView(ListView):
    template_name = 'blog_module/blog_list_page.html'
    model = Blog
    context_object_name = 'blog_list'
    ordering = ['-created_time']
    paginate_by = 6

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["latest_posts"] = Blog.objects.all().order_by('-created_time')[:5]
        context['categories'] = Category.objects.all()[:5]
        return context


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_module/blog_detail_page.html'


def category_view(request, category):
    articles = Category.objects.get(title__iexact=category).blog.all()
    context = {
        'articles': articles,
        'categories': Category.objects.all()[:5],
        "latest_posts": Blog.objects.all().order_by('-created_time')[:5],
        'category': category
    }
    return render(request, 'blog_module/category_page.html', context)







