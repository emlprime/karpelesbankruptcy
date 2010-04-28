from django.conf.urls.defaults import *

from django.contrib import admin

admin.autodiscover()

from karpelesbankruptcy.settings import MEDIA_ROOT

urlpatterns = patterns('',
    (r'^admin/(.*)$', admin.site.root),
    (r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)

urlpatterns += patterns('karpelesbankruptcy.content.views',
    (r'^$', 'index'),
    (r'^about_bankruptcy/$', 'about_bankruptcy'),
    (r'^loan_modifications/$', 'loan_modifications'),
    (r'^about/$', 'about'),
    (r'^resources/$', 'resources'),
    (r'^contact/$', 'contact'),
    (r'^chapter_7/$', 'chapter_7'),
    (r'^chapter_11/$', 'chapter_11'),
    (r'^chapter_13/$', 'chapter_13'),
    (r'^relief_from_stay/$', 'relief_from_stay'),
    (r'^disclaimer/$', 'disclaimer'),
)

urlpatterns += patterns('django.views.generic.simple',
    (r'^site_map/$', 'direct_to_template', {'template':'site_map.html'}),
)
