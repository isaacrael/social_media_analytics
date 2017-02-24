from django.conf.urls import include, url

from . import views


urlpatterns = [
#    url(r'^', include('send_email.urls')),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^success/', views.success, name='success')
]