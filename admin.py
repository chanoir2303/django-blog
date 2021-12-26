from django.contrib import admin

from .models import Article, Feedback, Tutorial


class FeedbackInline(admin.TabularInline):
    model = Feedback
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['previewed_text']}),
        (None, {'fields': ['vote']}),
        (None, {'fields': ['file']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [FeedbackInline]
    list_display = ('title', 'previewed_text', 'vote', 'file', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']


class TutorialAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
        (None, {'fields': ['previewed_text']}),
        (None, {'fields': ['vote']}),
        (None, {'fields': ['file']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('title', 'previewed_text', 'vote', 'file', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tutorial, TutorialAdmin)

