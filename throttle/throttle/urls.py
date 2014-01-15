from .views import (KannelMessageCreateView, KannelMessageDetailView,
                    KannelMessageListView)
from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^router/receive/', 'throttle.views.router_receive'),
    url(r'^receive/', 'throttle.views.receive'),
    #url(r'^admin/', include(admin.site.urls)),

    # web ui
    url(
        r'^$',
        KannelMessageListView.as_view(),
        name='message-list'
    ),
    url(
        r'new$',
        KannelMessageCreateView.as_view(),
        name='message-new'
    ),
    url(
        r'(?P<pk>\d+)/$',
        KannelMessageDetailView.as_view(),
        name='message-view'
    )
)

urlpatterns += staticfiles_urlpatterns()
