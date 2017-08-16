from django.conf.urls import url



from . import views

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^posts/$', views.PostsView.as_view(), name='posts'),
    url(r'^posts/(?P<posttypefilter>\w+)/$', views.PostByTypeView.as_view(), name='postbytype'),
    url(r'^posts/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='postdetail'),
    url(r'^about/$', views.About.as_view(), name='about'),
]
