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

# Create your views here.


def index(request):
    return render(request,'index.html')


def analytics(request):
    return render(request, 'analytics.html')


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