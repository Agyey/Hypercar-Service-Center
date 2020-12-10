from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render

services = [
    {
        'name': 'Change oil',
        'path': 'change_oil'
    },
    {
        'name': 'Inflate tires',
        'path': 'inflate_tires'
    },
    {
        'name': 'Get diagnostic test',
        'path': 'diagnostic'
    },
]

class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')

class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tickets\menu.html', context={'services': services})
