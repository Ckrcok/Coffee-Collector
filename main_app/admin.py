from django.contrib import admin
from .models import Coffee, Sugar, Flavor

# Register your models here.
admin.site.register(Coffee)
admin.site.register(Sugar)
admin.site.register(Flavor)
