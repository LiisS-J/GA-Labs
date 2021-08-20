from django.contrib import admin

# import your models here
from .models import Mug, Teatime

# Register your models here.
admin.site.register(Mug)
admin.site.register(Teatime)
