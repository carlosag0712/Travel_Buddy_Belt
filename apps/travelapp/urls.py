from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^travels$', views.travel_index, name='travels'),
    url(r'^travels/add$', views.render_travel_form),
    url(r'^travels/post$', views.travel_add),
    url(r'^travels/destination/(?P<travel_id>\d+)$', views.travel_details),
    url(r'^travels/join/(?P<travel_id>\d+)$', views.travel_join)
]
