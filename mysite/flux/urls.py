from django.urls import path

from .views import view_index, view_create_ticket, view_create_review, view_create_ticket_and_review

app_name = 'flux'

urlpatterns = [
    path('', view_index, name='home'),
    path('create/ticket', view_create_ticket, name='create_ticket'),
    path('create/review/<ticket_pk>', view_create_review, name='create_review'),
    path('create/ticketandreview/', view_create_ticket_and_review, name='create_ticket_and_review'),
]