from django.conf.urls import url
import gomaku.views as views
app_name = 'gomaku'
urlpatterns = [
    # url(r'register', views.register, ),
    url(r'login', views.login),
    url(r'^logout/$', views.logout),
    url(r'^User/$', views.UserList.as_view()),
    url(r'^User/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^Game/$', views.GameList.as_view()),
    url(r'^Game/(?P<pk>[0-9]+)/$', views.GameDetail.as_view()),
    url(r'^Friend/$', views.FriendList.as_view()),
    url(r'^Friend/(?P<pk>[0-9]+)/$', views.FriendDetail.as_view()),
]