from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=40)
    pub_date = models.DateTimeField(default=timezone.now())
    author = models.CharField(default='Admin', max_length=40)
    previewed_text = models.CharField(default='none', max_length=400)
    file = models.FileField(upload_to='article_file', null=True)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Tutorial(models.Model):
    title = models.CharField(max_length=40)
    pub_date = models.DateTimeField(default=timezone.now())
    author = models.CharField(default='Admin', max_length=40)
    previewed_text = models.CharField(default='none', max_length=400)
    file = models.FileField(upload_to='tutorial_file', null=True)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    feedback_text = models.TextField()

    def __str__(self):
        return self.feedback_text


class Link(models.Model):
    title = models.CharField(max_length=40)
    link = models.CharField(max_length=500)

    def __str__(self):
        return self.title
