from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', main, name='main'),
    url(r'^candidate/$', candidate, name='candidate'),
    url(r'^jedi/$', jedi, name='jedi'),
    url(r'^results/(?P<jedi_id>[0-9]+)/$', results, name="results"),
    url(r'^test/(?P<candidate_id>[0-9]+)/$', test, name="test"),
    url(r'^results/(?P<jedi_id>[0-9]+)/accept/(?P<candidate_id>[0-9]+)/$', accept, name="accept"),
    url(r'^padawans/$', all_padawans, name='padawans'),
    url(r'^padawans/more_one/$', more_one_padawan, name='more_one_padawan'),
]