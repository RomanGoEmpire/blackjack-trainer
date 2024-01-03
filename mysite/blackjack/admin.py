from django.contrib import admin

from .models import Card, HandHistory

admin.site.register([Card, HandHistory])

