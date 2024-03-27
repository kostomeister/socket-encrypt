from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'brand')
    list_filter = ('color', 'brand')
    search_fields = ('name', 'brand')


admin.site.register(Car, CarAdmin)
