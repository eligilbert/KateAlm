
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings

from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView



from .views import (
	general_main,
	general_immersion,
    general_events,
    general_school_year,
    general_programs,
	general_musicalsoulmates,
    general_harmonyyouth

)


urlpatterns = [
    url(r'^$', general_main, name="home"),
    url(r'^new-students/$', general_immersion, name="immersion"),
    url(r'^events/$', general_events, name="events"),
    url(r'^existing-students/$', general_school_year, name="school_year"),
    url(r'^programs/$', general_programs, name="programs"),
    url(r'^musicalsoulmates/$', general_musicalsoulmates, name="musicalsoulmates"),
    url(r'^harmonyyouth/$', general_harmonyyouth, name="harmonyyouth"),
    url('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('images/favicon.ico')))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
