from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

from karpelesbankruptcy.settings import MEDIA_ROOT

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^site_media/(.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
)

urlpatterns += patterns('django.views.generic.simple',
    (r'^$', 'direct_to_template', {'template':'index.html'}),
)
