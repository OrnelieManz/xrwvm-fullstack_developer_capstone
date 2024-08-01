from django.contrib import admin
from .models import CarMake, CarModel


# Register models 

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel 
    extra = 5

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['car_make','name', 'type', 'year', 'dealer']
    
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [CarModelInline]

# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)