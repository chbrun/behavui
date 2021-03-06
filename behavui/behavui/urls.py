from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', 'behavui.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^projects/', include('projects.urls')),
    url(r'^campaigns/', include('campaigns.urls')),
    url(r'^features/', include('features.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
