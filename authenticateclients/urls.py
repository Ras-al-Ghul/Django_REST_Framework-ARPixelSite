from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from authenticateclients import views

urlpatterns = [
    url(r'^uploaderclient/$', views.UploaderClientList.as_view(), name='uploaderclients'),
    url(r'^uploaderclient/(?P<pk>[0-9]+)/$', views.UploaderClientDetail.as_view(), name='uploaderclientsdetail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)