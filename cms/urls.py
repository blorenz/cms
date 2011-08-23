from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
url(r'^$', 'basecms.views.home', name='home'),
url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
url(r'^admin/', include(admin.site.urls)),
url(r'^tiny_mce/(?P<path>.*)$','django.views.static.serve',
{ 'document_root': '/virtualenvs/cms/tinymce/jscripts/tiny_mce/'}),
url(r"^search/$","search.views.search"),
url(r'^weblog/$', 'coltrane.views.entries_index'),
url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
            'coltrane.views.entry_detail'),
url(r'',include('django.contrib.flatpages.urls')),
)
