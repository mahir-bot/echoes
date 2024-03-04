from django.urls import include, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from stories import views as article_views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'account/', include('account.urls')),
    re_path(r'^story/', include('stories.urls')),
    re_path(r'^about/$', views.about),
    re_path(r'^$', article_views.story_list,name='home'),


]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('account/', include('account.urls')),
#     path('story/', include('stories.urls')),
#     path('about/', views.about),
#     path('', views.homepage),

# ]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
