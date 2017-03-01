from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from . models import Answer, Question
import random
import datetime
from django.utils.encoding import *
import django.template.context_processors
import matplotlib as plt
from pylab import *
from . processors import custom_processor


# Create your views here.





def index(request):
    #now = datetime.datetime.now()
    #context={'DATE_TIME':now}
    context = RequestContext(request, [custom_processor])
    return render(request, 'index.html', {'context':context})


def analytics(request):
    context = RequestContext(request, [custom_processor])
    return render(request, 'analytics.html', {'context':context})


def contact(request):
    return render(request, 'contact.html')


def twitter_sentiment(request):
    return render(request, 'twitter_sentiment.html')


def facebook_sentiment(request):
    return render(request, 'facebook_sentiment.html')


def youtube_sentiment(request):
    return render(request, 'youtube_sentiment.html')



def tumblr_sentiment(request):
    return render(request, 'tumblr_sentiment.html')


def plot(request):
    file_path = "../static/images/plot.png"
    plt.plot([1,2,4,50,2,1])
    plt.savefig("social_media_analytics_app/static/images/plot.png")
    img_path = {'PATH': file_path}
    return render(request, 'plot.html', img_path)