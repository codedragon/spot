from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^all-owners/$', 'stats.views.view_owners',
        name='view_owners'),
    url(r'^(.+)/$', 'stats.views.new_owner', name='new_owner'),
    url(r'^new$', 'stats.views.post_owner', name='post_owner'),

    # url(r'^rover/', include('rover.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^stats/', include('stats.urls'))
)
