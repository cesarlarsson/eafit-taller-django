from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eafit.views.home', name='home'),
    # url(r'^eafit/', include('eafit.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^encuestas/', include('encuestas.urls', namespace="encuestas")),
    url(r'^admin/', include(admin.site.urls)),
    #pagina por defecto
    (r"^$", include('encuestas.urls')),



)


urlpatterns += staticfiles_urlpatterns()