from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from clientupload import views

urlpatterns = [
    url(r'^imagetarget/$', views.ImageTargetList.as_view(), name='imagetargets'),
    url(r'^imagetarget/(?P<pk>[0-9]+)/$', views.ImageTargetDetail.as_view(), name='imagetargetsdetail'),
    url(r'^object3dtarget/$', views.Object3DTargetList.as_view(), name='object3dtargets'),
    url(r'^object3dtarget/(?P<pk>[0-9]+)/$', views.Object3DTargetDetail.as_view(), name='object3dtargetsdetail'),
    url(r'^texttarget/$', views.TextTargetList.as_view(), name='texttargets'),
    url(r'^texttarget/(?P<pk>[0-9]+)/$', views.TextTargetDetail.as_view(), name='texttargetsdetail'),
    url(r'^$', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)