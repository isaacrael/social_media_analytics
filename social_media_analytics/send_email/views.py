from django.shortcuts import render
# send_email/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

# create your own views here

def email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['gil@gilrael.com'],
            )
            return HttpResponseRedirect('success')
    else:
        form = ContactForm()
    return render(request, 'email.html', {'form': form})



def success(request):
    return render(request, 'success.html')

