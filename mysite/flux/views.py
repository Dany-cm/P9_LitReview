from itertools import chain

from django.contrib.auth.decorators import login_required
from django.db.models import Value, CharField
from django.shortcuts import render, redirect

# Create your views here.
from .models import Ticket


@login_required
def view_index(request):
    all_tickets = Ticket.objects.all()
    all_tickets = all_tickets.annotate(content_type=Value('TICKET', CharField()))

    ticket = sorted(chain(all_tickets), key=lambda instance: instance.time_created, reverse=True)
    return render(request, 'home.html', {'tickets': ticket})


@login_required
def view_create_ticket(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        ticket = Ticket(title=title, description=description, image=image, user=request.user)
        ticket.save()

        return redirect('flux:home')
    else:
        return render(request, 'create_ticket.html')
