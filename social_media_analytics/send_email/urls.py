from django.conf.urls import include, url

from . import views

urlpatterns = [
#    url(r'^', include('send_email.urls')),
    url(r'^email/', views.email, name='email'),
    url(r'^success/', views.success, name='success'),
]