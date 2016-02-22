from django.conf.urls import url, include, patterns
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'livro.views.index',name='index'),
    url(r'^save/$','livro.views.save',name='livro.save'),
    url(r'^edit/(?P<livro_id>\d+)[/]$','livro.views.edit', name='livro.edit'),
    url(r'^remove/(?P<livro_id>\d+)[/]$','livro.views.remove', name='livro.remove'),
)
