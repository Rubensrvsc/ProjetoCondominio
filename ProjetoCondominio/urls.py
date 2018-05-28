from django.conf.urls import patterns, include, url
from AppCondominio import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProjetoCondominio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^array/$', views.index),
    url(r'^boot/$',views.boot),
    url(r'^form/$',views.apartForm)
 )
