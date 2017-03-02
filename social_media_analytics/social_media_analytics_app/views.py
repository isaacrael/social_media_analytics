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
    labels = " "
    file_path_plot = "../static/images/plot.png"
    plt.plot([1,2,4,50,2,1,2,78])
    plt.savefig("social_media_analytics_app/static/images/plot.png")
    img_path_plot = {'PATH_PLOT': file_path_plot}
    return render(request, 'plot.html', img_path_plot)


def piechart(request):
    """
===============
Basic pie chart
===============

Demo of a basic pie chart plus a few additional features.

In addition to the basic pie chart, this demo shows a few optional features:

    * slice labels
    * auto-labeling the percentage
    * offsetting a slice with "explode"
    * drop-shadow
    * custom start angle

Note about the custom start angle:

The default ``startangle`` is 0, which would start the "Frogs" slice on the
positive x-axis. This example sets ``startangle = 90`` such that everything is
rotated counter-clockwise by 90 degrees, and the frog slice starts on the
positive y-axis.
"""
    file_path_pie_chart = "../static/images/pie_chart.png"

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Tumblr', 'Twitter', 'Facebook', 'Youtube'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Twitter')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig("social_media_analytics_app/static/images/pie_chart.png")
    img_path_pie_chart = {'PATH_PIE_CHART': file_path_pie_chart}
    return render(request, 'pie_chart.html', img_path_pie_chart)