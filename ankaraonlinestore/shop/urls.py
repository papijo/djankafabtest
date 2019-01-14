from django.conf.urls import url
from django.urls import include, path
from . import views

app_name = 'shop'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    path('aboutus/', views.aboutus, name = 'aboutus'),
    path('contactus/', views.contactus, name = 'contactus'),
    path('privacypolicy', views.privacypolicy, name = 'privacypolicy'),
    path('shop/', views.product_list, name='product_list'),
    #path('shop/<category_slug>/', views.product_list, name = 'product_list_by_category'),
    url(r'^shop/categories/(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^shop/types/(?P<type_slug>[-\w]+)/$', views.product_list, name='product_list_by_type'),
    #path('shop/<type_slug>/', views.product_list, name='product_list_by_type'),
    url(r'^shop/brands/(?P<brand_slug>[-\w]+)/$', views.product_list, name='product_list_by_brand'),
    #path('shop/<brand_slug>/', views.product_list, name = 'product_list_by_brand'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]