from django.conf.urls import patterns, url
from .views import qunit_views, qunit_tests_list_json


# Add registered qunit tests
urlpatterns = patterns('',
    *(
        url(r'^jstest/%s' % name, qunit_view, name='jstest_%s' % name)
        for name, qunit_view in qunit_views.iteritems()
    )
)

# List views as json
urlpatterns += patterns('', url(r'^jstest_list', qunit_tests_list_json))
