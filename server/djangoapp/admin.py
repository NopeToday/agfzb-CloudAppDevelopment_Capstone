from django.contrib import admin
from .models import CarMake, CarModel
# from .models import related models


# Register your models here.
admin.site.register(CarMake)

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
# Register models here
