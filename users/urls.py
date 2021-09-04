# definition url model

from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # login interface
    url(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'),
    # login out
    url(r'^logout/$', views.logout_view, name='logout'),
    # register interface
    url(r'^register/$', views.register, name='register'),
]
