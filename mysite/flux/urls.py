from django.urls import path

from .views import view_index, view_create_ticket

app_name = 'flux'

urlpatterns = [
    path('', view_index, name='home'),
    path('create/ticket', view_create_ticket, name='create_ticket'),
]
