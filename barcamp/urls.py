from django.conf.urls import patterns, include, url

from core.views import HomeView, RegisterView, LoginView, DashboardView, \
                       CampView, CampListView, \
                       SessionCreateView, SessionView \

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'barcamp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/', DashboardView.as_view(), name='dashboard'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^camps/$', CampListView.as_view(), name='camp_list'),
    url(r'^(?P<camp>[-_a-zA-Z0-9]+)/(?P<session>[-_a-zA-Z0-9]+)/$', SessionView.as_view(), name='session_view'),
    url(r'^(?P<camp>[-_a-zA-Z0-9]+)/session/create/$', SessionCreateView.as_view(), name='session_create'),
    url(r'^(?P<camp>[-_a-zA-Z0-9]+)/$', CampView.as_view(), name='camp'),
    url(r'^$', HomeView.as_view(), name='home_view'),
)
