from django.urls import path

from .views import view_index

app_name = 'flux'

urlpatterns = [
    path('', view_index, name='home'),
]
