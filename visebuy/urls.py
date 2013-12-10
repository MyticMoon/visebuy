from django.conf.urls import patterns, url

from visebuy import views
from visebuy import search_handle

urlpatterns = patterns('',
    url(r'^$', views.base, name='homepage'),
    url(r'^base/$', views.base, name='base'),
    url(r'^page/(?P<offset>.*)/$', views.detailpage, name='detailpage'),
    url(r'^search/create/$', search_handle.search),
    url(r'^searchimageurl/$', search_handle.search_by_imageurl),
    url(r'^searchproductid/$', search_handle.search_by_productid),
    url(r'^searchbyimage/$', search_handle.search_by_image),
    url(r'^demohome/$', views.demo_homepage),
    url(r'^demosearch/$', views.demo_searchpage),

)
