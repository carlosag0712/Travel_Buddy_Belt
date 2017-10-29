from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.redirect_to_main),
    url(r'^main$', views.index),
    url(r'^register$', views.register),
    url(r'^register/submit$', views.submit_registration),
    url(r'^register/success$', views.success_registration),
    url(r'^login$', views.render_login, name="login"),
    url(r'^login/submit$', views.login),
    url(r'^logout$', views.log_out)
]
