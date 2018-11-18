import requests, json
from django.shortcuts import render
from sunshine.models import Contact
# Create your views here.

from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        response = requests.get(
            'http://api.icndb.com/jokes/random?firstName=' + firstname + '&amp;lastName=' + lastname)
        json_data = response.json()
        joke = json_data.get('value').get('joke')
        context = {'joker': joke}

        print(joke)
        return render(request, 'mysite/index.html', context)
    else:
        firstname = 'John'
        lastname = 'Doe'
        response = requests.get(
            'http://api.icndb.com/jokes/random?firstName=' + firstname + '&amp;lastName=' + lastname)
        json_data = response.json()
        joke = json_data.get('value').get('joke')
        context = {'joker': joke}
        return render(request, 'mysite/index.html', context)


def portfolio(request):
    return render(request, 'mysite/portfolio.html')


def contact(request):
    if request.method == 'POST':
        email_r = request.POST['email']
        subject_r = request.POST['subject']
        message_r = request.POST['message']

        contact_r = Contact(email=email_r, subject=subject_r, message=message_r)
        contact_r.save()
        return render(request, 'mysite/thank.html')
    else:
        return render(request, 'mysite/contact.html')


def demo(request):
    return render(request, 'mysite/demo.html')
