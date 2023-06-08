from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.base import View
from django.views.generic.list import ListView

from podcast_module.models import Podcast


# Create your views here.


class PodcastListView(ListView):
    model = Podcast
    template_name = 'podcast_module/podcast_list.html'
    context_object_name = 'podcasts'
    ordering = ['-created_time']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context["last_podcast"] = Podcast.objects.last()
        context["AI"] = Podcast.objects.filter(season__number=1).order_by('-created_time')
        context['english'] = Podcast.objects.filter(season__number=100).order_by('-created_time')
        return context


class PodcastDetailView(DetailView):
    model = Podcast
    template_name = 'podcast_module/podcast_detail.html'
