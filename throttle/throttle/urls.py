from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^router/receive/', 'throttle.views.router_receive'),
    url(r'^receive/', 'throttle.views.receive'),
    #url(r'^admin/', include(admin.site.urls)),
)
