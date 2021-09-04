'''Define URL mode'''
from django.conf.urls import url
from . import views

urlpatterns = [
    # homepage
    url(r'^$', views.index, name='index'),
    # all topic
    url(r'^topics/$', views.topics, name='topics'),
    # Specific topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # Web page for adding new topics
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # Web page for adding new entry(条目)
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # Web page for editing entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]

