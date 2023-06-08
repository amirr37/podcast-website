from django.shortcuts import render
from django.views.generic.base import View

from blog_module.models import Blog
from podcast_module.models import Podcast


# Create your views here.


class IndexPageView(View):
    def post(self, request):
        context = {'last_podcast': Podcast.objects.last(),
                   'last_5_podcasts:': Podcast.objects.order_by('created_time')[-5:],
                   'AI_podcasts': Podcast.objects.filter(season__number=1),
                   'latest_posts': Blog.objects.all().order_by('-created_time')[:5],
                   }
        return render(request, 'home_module/index_page.html')

    def get(self, request):
        context = {'last_podcast': Podcast.objects.latest('created_time'),
                   'last_5_podcasts:': Podcast.objects.order_by('created_time'),
                   'AI_podcasts': Podcast.objects.filter(season__number=1),
                   'latest_posts': Blog.objects.all().order_by('-created_time')[:5],
                   }
        return render(request, 'home_module/index_page.html', context)
