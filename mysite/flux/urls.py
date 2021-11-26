from django.urls import path

from .views import view_index, view_create_ticket, view_create_review, view_create_ticket_and_review, \
    view_modify_ticket, view_delete_ticket, view_my_posts, view_subscription, view_unsubscribe, view_modify_review, \
    view_delete_review

app_name = 'flux'

urlpatterns = [
    path('', view_index, name='home'),
    path('create/ticket', view_create_ticket, name='create_ticket'),
    path('create/review/<ticket_pk>', view_create_review, name='create_review'),
    path('create/ticketandreview/', view_create_ticket_and_review, name='create_ticket_and_review'),
    path('modify/ticket/<ticket_pk>', view_modify_ticket, name='modify_ticket'),
    path('modify/review/<review_pk>', view_modify_review, name='modify_review'),
    path('delete/ticket/<ticket_pk>', view_delete_ticket, name='delete_ticket'),
    path('delete/review/<review_pk>', view_delete_review, name='delete_review'),
    path('posts', view_my_posts, name='posts'),
    path('subscription', view_subscription, name='subscription'),
    path('unsubscribe/<user>', view_unsubscribe, name='unsubscribe'),
]
