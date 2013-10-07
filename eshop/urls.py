from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eshop.views.home', name='home'),
    # url(r'^eshop/', include('eshop.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^query$', 'order.views.query'),
    url(r'^cancelorder$', 'order.views.order'),
    url(r'^order$', 'order.views.order'),
    url(r'^$', 'order.views.index', name='home'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                'document_root': settings.MEDIA_ROOT,
            }),    
)
