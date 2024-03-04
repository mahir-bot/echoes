
from django.urls import re_path
from . import views

app_name = 'stories'

urlpatterns = [

    re_path(r'^$', views.story_list, name='list'),
    re_path(r'^create/$', views.story_create, name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.story_detail, name='detail'),

    # path('', views.story_list,name='list'),
    # path('<slug:slug>/', views.story_detail, name='detail'),
]
