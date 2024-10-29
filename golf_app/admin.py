from django.contrib import admin
from .models import Golfclub, Member, Tournament

# Register your models here.
admin.site.register(Golfclub)
admin.site.register(Member)
admin.site.register(Tournament)