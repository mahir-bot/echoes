from django.urls import re_path
from . import views


app_name = 'account'

urlpatterns = [
    re_path(r'^signup/$', views.signupView, name='signup'),
    re_path(r'^login/$', views.loginView, name='login'),
    re_path(r'^logout/$', views.logoutView, name='logout'),
]
