from django.conf.urls import url, include

from apps.registration.views import RegisterUser, ProfileDetail, ProfileUpdate

app_name = 'registration'
urlpatterns = [
    url(r'^registrar$', RegisterUser.as_view(), name='registration'),
    url(r'^profile/(?P<pk>\d+)$', ProfileDetail.as_view(), name='profile'),
    url(r'^profile/update/(?P<pk>\d+)$', ProfileUpdate.as_view(), name='profile_update'),

]