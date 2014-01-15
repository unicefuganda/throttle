from .views import KannelMessageCreateView, KannelMessageListView
from django.conf.urls import include, patterns, url

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
    )
)
