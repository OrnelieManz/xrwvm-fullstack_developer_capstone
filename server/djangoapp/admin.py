from django.contrib import admin
from .models import CarMake, CarModel


# Register models 

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = Carmodel 
    extra = 5
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['car_make','name', 'type', 'year', 'dealer']
    inlines = [LessonInline]
# CarMakeAdmin class with CarModelInline

# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)