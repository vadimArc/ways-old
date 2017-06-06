from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^register/$',views.register_user, name='register'),
    url(r'^cities/$', views.city_add, name='city_search'),
    url(r'^addlist/(?P<city_name>.*)/$', views.add_list, name='add_list'),
    url(r'^profile/$', views.profile, name = 'profile'),
    url(r'^(?P<city_name>.*)/places/$', views.user_places, name='user_places'),
    url(r'^(?P<city_name>.*)/(?P<venue_id>.*)/save/$', views.add_place, name='add_place'),
    url(r'^friends/$', views.user_friends, name='friends')
]
