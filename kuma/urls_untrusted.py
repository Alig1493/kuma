from django.conf import settings
from django.conf.urls import include, url

from kuma.core import views as core_views
from kuma.landing.views import robots_txt

handler403 = core_views.handler403
handler404 = core_views.handler404
handler500 = core_views.handler500

urlpatterns = [
    url('', include('kuma.attachments.urls')),
    url(r'^docs', include('kuma.wiki.urls_untrusted')),
    url(r'^robots.txt', robots_txt, name='robots_txt'),
]

if getattr(settings, 'DEBUG_TOOLBAR_INSTALLED', False):
    import debug_toolbar
    urlpatterns.append(
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
