from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^travels/', include('travels.urls')),
    url(r'^admin/', admin.site.urls),
]
