from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from blog_chanoir2303 import settings
from . import views

app_name = 'blog'
urlpatterns = [
    path('news', views.NewsView.as_view(), name='news'),
    path('tutorials/', views.TutorialView.as_view(), name='tutorials'),
    path('archives/', views.ArchiveView.as_view(), name='archives'),
    path('formAdmin/', views.formAdmin, name='formAdmin'),
    path('login/', LoginView.as_view(template_name='blog/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html', next_page='blog:news'), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
