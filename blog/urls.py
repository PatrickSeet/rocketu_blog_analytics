from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^blog/$', 'blog.views.blog', name='blog'),
    url(r'^blog/(\d+)/$', 'blog.views.post', name='post'),
    url(r'^main/$', 'blog.views.main', name='main'),
    url(r'^postwithtags/(\d+)/$', 'blog.views.postwithtags', name='postwithtags'),
    url(r'^error/$', 'blog.views.error', name='error'),

)
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)