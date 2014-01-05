from django.conf.urls import patterns, include, url

from core.views import HomeView, RegisterView, DashboardView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'barcamp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/', DashboardView.as_view(), name='dashboard'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^$', HomeView.as_view(), name='home_view'),
)
