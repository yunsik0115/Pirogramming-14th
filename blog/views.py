from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from django.conf import settings


from blog.models import Post

class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html' # 왜 기본값 세팅이 post_list가 되는건가?
    context_object_name = 'posts'
    paginate_by = 2 # 2항목당 1페이지

class PostDV(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.slug}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modified_at'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modified_at'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modified_at'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modified_at'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modified_at'

class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context




# Create your views here.
