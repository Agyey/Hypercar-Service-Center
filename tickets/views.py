from django.views import View
from django.http.response import HttpResponse
from django.shortcuts import render
from collections import deque

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

oil_change_queue = deque()
inflating_queue = deque()
diagnostic_queue = deque()
ticket_number = 0

class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(View):
    def get(self, request, *args, **kwargs):
        return render(request, r'tickets\menu.html', context={'services': services})


class GetTicketView(View):
    def get(self, request, *args, **kwargs):
        global ticket_number, oil_change_queue, inflating_queue, diagnostic_queue
        service_name = kwargs['service_name']
        ticket_number += 1
        wait_time = 0
        if service_name == 'change_oil':
            wait_time = len(oil_change_queue) * 2
            oil_change_queue.appendleft(ticket_number)
        elif service_name == 'inflate_tires':
            wait_time = len(oil_change_queue) * 2 + len(inflating_queue) * 5
            inflating_queue.appendleft(ticket_number)
        elif service_name == 'diagnostic':
            wait_time = len(oil_change_queue) * 2 + len(inflating_queue) * 5 + len(diagnostic_queue) * 30
            diagnostic_queue.appendleft(ticket_number)
        return render(request, r'tickets\get_ticket.html', context={
            'ticket_number': ticket_number,
            'wait_time': wait_time
        })
