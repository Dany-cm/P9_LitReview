from django.urls import path

from .views import view_index, view_register, view_login, view_logout

app_name = 'accounts'

urlpatterns = [
    path('', view_index, name='index'),
    path('register/', view_register, name='register'),
    path('login/', view_login, name='login'),
    path('logout/', view_logout, name='logout'),
]
