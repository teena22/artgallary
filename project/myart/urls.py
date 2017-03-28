from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^contact/', views.Message, name='message'),
    url(r'^user/(?P<username>.+)', views.painting_upload, name='upload'),
    url(r'^(?P<user_id>[0-9]+)/paintings$', views.Show_painting, name='painting'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^deluser/', views.del_user, name='del'),
    url(r'^pic/', views.pic_upload, name='pic'),
    url(r'^search-artist/$', views.search_artist),
    url(r'^search/$', views.search),
]
