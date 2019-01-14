from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    #path('blog/<tag_slug>/', views.post_list, name = 'post_list_by_tag'),
    url(r'^tags/(?P<tag_slug>[-\w]+)/$', views.post_list, name='post_list_by_tag'),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail')
]