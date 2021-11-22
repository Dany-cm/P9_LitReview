from django.contrib import admin

# Register your models here.
from .models import Ticket, UserFollows, Review

admin.site.register(Ticket)
admin.site.register(Review)
admin.site.register(UserFollows)
