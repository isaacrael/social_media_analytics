from django.conf.urls import include, url

from . import views


urlpatterns = [
    # ex: /quiz/
    url(r'^', include('send_email.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^analytics/', views.analytics, name='analytics'),
    url(r'^twitter/', views.twitter_sentiment, name='twitter_sentiment'),
    url(r'^facebook/', views.facebook_sentiment, name='facebook_sentiment'),
    url(r'^youtube/', views.youtube_sentiment, name='youtube_sentiment'),
    url(r'^tumblr/', views.tumblr_sentiment, name='tumblr_sentiment'),
#    url(r'^contact/', views.contact, name='contact')
    #url(r'^resources/', views.git_resources, name='resources'),
    # ex: /quiz/5/
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /quiz/5/results/
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /quiz/5/vote/
# Note: the answers url is not being used in the app but is left here
# as an example for future versions
#    url(r'^(?P<question_id>[0-9]+)/answer/$', views.answer, name='answer'),
]


