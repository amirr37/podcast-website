from django.urls import path
from podcast_module import views

urlpatterns = [path('podcasts', views.PodcastListView.as_view(), name='podcasts_list_page'),
               path('podcasts/<slug:slug>', views.PodcastDetailView.as_view(), name='podcast_detail_page'),
               ]
