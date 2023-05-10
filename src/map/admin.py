from django.contrib import admin

from .models import User, Map, LandMark

admin.site.register(User)
admin.site.register(Map)
admin.site.register(LandMark)