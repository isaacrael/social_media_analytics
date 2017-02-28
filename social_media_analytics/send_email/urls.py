from django.conf.urls import include, url

from . import views


urlpatterns = [
#    url(r'^', include('send_email.urls')),
    url(r'^contact/$', views.email, name='email'),
    url(r'^contact/success/$', views.success, name='success')
]