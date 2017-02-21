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



# This context processor function takes the request
# object and returns a dictionary of context variables
# to be made available to all templates.  Note: this
# context processor is not being used in this app but is
# included as an example for future versions

def get_current_time(request):
  # Create a 'context' dictionary,
  # populate it with the current time
  # and return it
  context = {}
  context['current_time'] = datetime.datetime.now()
  return context


# Note the index page used in the index function below tells the computer
# user about the application and what it is meant to be used for

def index(request):
    return render(request, 'index.html')


def git_quiz(request):
    latest_question_list = Question.objects.order_by('?')
#    value = latest_question_list[0]
#    q = smart_text(value)
    context = {'latest_question_list': latest_question_list}
    return render(request, 'giturdone_quiz/index.html', context)


def git_resources(request):
        return render(request, 'giturdone_quiz/resources.html')

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'giturdone_quiz/detail.html', {'question': question})

"""
# Note: The answer function below is not being used but is left here
# as an example for future versions of the application and may be able
# to be used to implement a way to show a computer users test score based
# on the number of questions answered correctly vs. total questions responded to

def answer(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.answer_set.get(pk=request.POST['answer'])
    except (KeyError, Answer.DoesNotExist):
        # Redisplay the question answer form.
        return render(request, 'giturdone_quiz/detail.html', {
            'question': p,
            'error_message': "You didn't select an answer.",
        })
    else:
        selected_choice.answers += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('giturdone_quiz:results', args=(p.id,)))

"""

def results(request, question_id):
    latest_question_list = Question.objects.order_by('?')
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=question_id)
        user_answer = request.POST.get('textfield', None)
        # Get the question object
        q = Question.objects.get(pk=question_id)
        # Get all the answers associated with the question object
        a = q.answer_set.all()
        # Get the first element in the list of answers
        value = a[0]
        # smart_text is a django utility that converts an object to a unicode string
        correct_answer = smart_text(value)
        context = {'latest_question_list': latest_question_list, 'answer': user_answer, 'question': question, 'correct_answer': correct_answer}
        value = "gil"
    return render(request, 'giturdone_quiz/results.html', context)


