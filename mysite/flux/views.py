from itertools import chain

from django.contrib.auth.decorators import login_required
from django.db.models import Value, CharField
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Ticket, Review


@login_required
def view_index(request):
    all_tickets = Ticket.objects.all()

    all_tickets = all_tickets.annotate(content_type=Value('TICKET', CharField()))

    reviewed_tickets_ids = get_reviewed_tickets_id(request)

    all_reviewed_tickets = all_tickets.filter(id__in=reviewed_tickets_ids).annotate(
        state=Value('REVIEWED', CharField()))
    all_unreviewed_tickets = all_tickets.exclude(id__in=all_reviewed_tickets).annotate(
        state=Value('UNREVIEWED', CharField()))

    all_reviews = Review.objects.all()
    all_reviews = all_reviews.annotate(content_type=Value('REVIEW', CharField()))

    ticket = sorted(chain(all_unreviewed_tickets, all_reviewed_tickets, all_reviews),
                    key=lambda instance: instance.time_created, reverse=True)
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


@login_required
def view_create_review(request, ticket_pk):
    ticket = get_object_or_404(Ticket, pk=ticket_pk)
    if request.method == 'POST':
        headline = request.POST.get('headline')
        body = request.POST.get('body')
        rating = request.POST.get('rating')

        review = Review(headline=headline, body=body, rating=rating, ticket=ticket, user=request.user)
        review.save()

        return redirect('flux:home')
    else:
        return render(request, 'create_review.html', {'ticket': ticket})


@login_required
def get_reviewed_tickets_id(request):
    all_reviews = Review.objects.all()
    return [review.ticket.id for review in all_reviews]
