from django.contrib import admin

# import your models here
from .models import Makeup, Reviews, Dupe

# Register your models here
admin.site.register(Makeup)
admin.site.register(Reviews)
admin.site.register(Dupe)

