from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic

from .models import Article, Tutorial
from .templates.blog.form import ArticleForm, TutorialForm


class NewsView(generic.ListView):
    template_name = 'blog/news.html'
    context_object_name = 'latest_article_list'

    def get_queryset(self):
        """Return the last 6 published article_file"""
        return Article.objects.order_by('-pub_date')[:6]


class TutorialView(generic.ListView):
    template_name = 'blog/tutorials.html'
    context_object_name = 'latest_tutorial_list'

    def get_queryset(self):
        """Return tutorial list"""
        return Tutorial.objects.order_by('-pub_date')


class ArchiveView(generic.ListView):
    template_name = 'blog/archives.html'
    context_object_name = 'archive_list'

    def get_queryset(self):
        return Article.objects.order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super(ArchiveView, self).get_context_data(**kwargs)
        context['article'] = Article.objects.all().order_by('-pub_date')
        context['tutorial'] = Tutorial.objects.all().order_by('-pub_date')
        context['all'] = list(context['article']) + list(context['tutorial'])
        return context


@login_required
def formAdmin(request):
    form_article = ArticleForm()
    if request.method == 'POST':
        print(request.POST)
        form_article = ArticleForm(request.POST, request.FILES)
        if form_article.is_valid():
            form_article.save()

    context = {
        'form_article': form_article,
    }
    return render(request, 'blog/form.html', context)
