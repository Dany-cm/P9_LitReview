from django.urls import path

from .views import view_index, view_create_ticket, view_create_review, view_create_ticket_and_review, \
    view_modify_ticket, view_delete_ticket

app_name = 'flux'

urlpatterns = [
    path('', view_index, name='home'),
    path('create/ticket', view_create_ticket, name='create_ticket'),
    path('create/review/<ticket_pk>', view_create_review, name='create_review'),
    path('create/ticketandreview/', view_create_ticket_and_review, name='create_ticket_and_review'),
    path('modify/ticket/<ticket_pk>', view_modify_ticket, name='modify_ticket'),
    path('delete/ticket/<ticket_pk>', view_delete_ticket, name='delete_ticket'),
]