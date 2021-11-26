from itertools import chain

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Value, CharField, Q
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Ticket, Review, UserFollows


@login_required
def view_index(request):
    user_follow = User.objects.filter(followed_by__in=UserFollows.objects.filter(user=request.user))

    all_tickets = Ticket.objects.filter(Q(user__in=user_follow) | Q(user=request.user))
    all_tickets = all_tickets.annotate(content_type=Value('TICKET', CharField()))

    reviewed_tickets_ids = get_reviewed_tickets_id(request)

    all_reviewed_tickets = all_tickets.filter(id__in=reviewed_tickets_ids).annotate(
        state=Value('REVIEWED', CharField()))
    all_unreviewed_tickets = all_tickets.exclude(id__in=all_reviewed_tickets).annotate(
        state=Value('UNREVIEWED', CharField()))

    all_reviews = Review.objects.filter(Q(user__in=user_follow) | Q(user=request.user))
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
        return render(request, 'create_review.html', {'ticket': ticket, 'rating': range(6)})


def get_reviewed_tickets_id(request):
    all_reviews = Review.objects.all()
    return [review.ticket.id for review in all_reviews]


@login_required
def view_create_ticket_and_review(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        headline = request.POST.get('headline')
        body = request.POST.get('body')
        rating = request.POST.get('rating')

        ticket = Ticket(title=title, description=description, image=image, user=request.user)
        review = Review(headline=headline, body=body, rating=rating, ticket=ticket, user=request.user)
        ticket.save()
        review.save()
        return redirect('flux:home')
    else:
        return render(request, 'create_ticket_and_review.html')


@login_required
def view_modify_ticket(request, ticket_pk):
    ticket = get_object_or_404(Ticket, pk=ticket_pk)
    if request.method == 'POST':
        ticket.title = request.POST.get('title')
        ticket.description = request.POST.get('description')
        ticket.image = request.FILES.get('image')

        ticket.save()
        return redirect('flux:home')
    return render(request, 'modify_ticket.html', {'ticket': ticket})


@login_required
def view_modify_review(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'POST':
        review.headline = request.POST.get('headline')
        review.body = request.POST.get('body')
        review.rating = request.POST.get('rating')

        review.save()
        return redirect('flux:home')
    return render(request, 'modify_review.html', {'review': review, 'rating': range(6)})


@login_required
def view_delete_ticket(request, ticket_pk):
    delete_ticket = get_object_or_404(Ticket, id=ticket_pk)

    if delete_ticket.image:
        delete_ticket.image.delete()
    delete_ticket.delete()

    return redirect('flux:home')


@login_required
def view_delete_review(request, review_pk):
    Review.objects.filter(id=review_pk).delete()
    return redirect('flux:home')


@login_required
def view_my_posts(request):
    all_tickets = Ticket.objects.filter(user=request.user)
    all_tickets = all_tickets.annotate(content_type=Value('TICKET', CharField()))

    all_reviews = Review.objects.filter(user=request.user)
    all_reviews = all_reviews.annotate(content_type=Value('REVIEW', CharField()))

    ticket = sorted(chain(all_tickets, all_reviews), key=lambda instance: instance.time_created, reverse=True)
    return render(request, 'posts.html', {'tickets': ticket})


@login_required
def view_subscription(request):
    user_follows = UserFollows.objects.filter(user=request.user)
    user_followed = UserFollows.objects.filter(user=request.user)

    if request.method == 'POST':
        user = request.POST.get('username')

        try:
            user_to_follow = User.objects.get(username=user)
            if user_to_follow == request.user:
                messages.error(request, 'Vous ne pouvez pas vous ajouter vous-même !')
                return redirect('flux:subscription')
        except User.DoesNotExist:
            messages.error(request, "Le nom de l'utilisateur est incorrect")
            return redirect('flux:subscription')
        else:
            subscription = UserFollows(user=request.user, followed_user=user_to_follow)
            subscription.save()

    return render(request, 'subscription.html', {'user_follows': user_follows, 'user_followed': user_followed})


@login_required
def view_unsubscribe(request, user):
    user_to_remove = User.objects.get(username=user)
    UserFollows.objects.get(followed_user_id=user_to_remove.id, user_id=request.user.id).delete()
    return redirect('flux:subscription')
