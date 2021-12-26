from django.forms import ModelForm
from blog.models import Article, Tutorial


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'file', 'previewed_text']


class TutorialForm(ModelForm):
    class Meta:
        model = Tutorial
        fields = ['title', 'author', 'file', 'previewed_text']


