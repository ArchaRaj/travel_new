from django.contrib import admin

# Register your models here.
from .models import Place
from .models import Place2
admin.site.register(Place)
admin.site.register(Place2)