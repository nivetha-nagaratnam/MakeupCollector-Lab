from django.contrib import admin

# import your models here
from .models import Makeup, Reviews

# Register your models here
admin.site.register(Makeup)

admin.site.register(Reviews)

