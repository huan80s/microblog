from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns+=patterns('',
    url(r'^sblog/',include('sblog.urls')),
    )
urlpatterns += patterns((''),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/home/whoo/djcode/work/blog/static/'}
    ),
)

urlpatterns += patterns('',
    (r'^comments/', include('django.contrib.comments.urls')),
)
